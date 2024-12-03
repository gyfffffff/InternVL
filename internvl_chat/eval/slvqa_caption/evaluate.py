import argparse
import itertools
import json
import os
import random
import subprocess
import time
from functools import partial
from typing import Optional

import torch
from internvl.model import load_model_and_tokenizer
from internvl.train.dataset import build_transform, dynamic_preprocess
from PIL import Image
from slvqa_evaluator import SLVQANLGEvaluator
from tqdm import tqdm
import datetime

ds_collections = {
    'slvqa_caption_ar': {
        'test': 'data/SLVQA/AR/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },
    'slvqa_caption_hu': {
        'test': 'data/SLVQA/HU/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },    
}


def evaluate_exact_match_accuracy(entries):
    scores = []
    for elem in entries:
        if isinstance(elem['annotation'], str):
            elem['annotation'] = [elem['annotation']]
        score = max([
            (1.0 if
             (elem['answer'].strip().lower() == ann.strip().lower()) else 0.0)
            for ann in elem['annotation']
        ])
        scores.append(score)
    return sum(scores) / len(scores)


def collate_fn(batches, tokenizer):
    pixel_values = torch.cat([_['pixel_values'] for _ in batches], dim=0)
    questions = [_['question'] for _ in batches]
    question_ids = [_['question_id'] for _ in batches]
    annotations = [_['annotation'] for _ in batches]

    return pixel_values, questions, question_ids, annotations

class VQADataset(torch.utils.data.Dataset):
    def __init__(self, dataset_name, prompt, few_shot, input_size=224, dynamic_image_size=False, use_thumbnail=False, max_num=6):
        self.prompt = prompt
        self.input_size = input_size
        self.dynamic_image_size = dynamic_image_size
        self.use_thumbnail = use_thumbnail
        self.max_num = max_num
        self.few_shot = few_shot
        # if self.few_shot > 0:
        #    self.train = open(ds_collections[dataset_name]['train'], 'r').readlines()
        self.transform = build_transform(is_train=False, input_size=input_size)
        self.dataset_name = dataset_name        
        self.data = []
        with open(ds_collections[dataset_name]['test'], 'r', encoding="utf-8") as f:
            for line in f:
                self.data.append(json.loads(line))
        self.data = self.data[:100]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        data = self.data[idx]
        question_id = data['image']
        question = data['question']
        annotation = data.get('answer', None)
        root_dir = f"/mnt/workspace/gaoyufei/InternVL/internvl_chat/data/SLVQA/{args.language}/images"
        image = os.path.join(root_dir, data['image'])
        image = Image.open(image).convert('RGB')
        if self.dynamic_image_size:
            images = dynamic_preprocess(image, image_size=self.input_size,
                                        use_thumbnail=self.use_thumbnail,
                                        max_num=self.max_num)
        else:
            images = [image]   
        pixel_values = [self.transform(image) for image in images]  
        pixel_values = torch.stack(pixel_values)   
        if len(self.prompt) != 0:
            question = question + ' ' + self.prompt

        return {
            'question_id': question_id,
            'question': question,
            'pixel_values': pixel_values,
            'annotation': annotation
        }

class InferenceSampler(torch.utils.data.sampler.Sampler):
    def __init__(self, size):
        self._size = int(size)
        assert size > 0
        self._rank = torch.distributed.get_rank()
        self._world_size = torch.distributed.get_world_size()
        self._local_indices = self._get_local_indices(size, self._world_size, self._rank)

    @staticmethod
    def _get_local_indices(total_size, world_size, rank):
        shard_size = total_size // world_size
        left = total_size % world_size
        shard_sizes = [shard_size + int(r < left) for r in range(world_size)]

        begin = sum(shard_sizes[:rank])
        end = min(sum(shard_sizes[:rank + 1]), total_size)
        return range(begin, end)

    def __iter__(self):
        yield from self._local_indices

    def __len__(self):
        return len(self._local_indices)


def evaluate_chat_model():
    base_prompt = ''
    random.seed(args.seed)
    summaries = []

    for ds_name in args.datasets:
        if 'nlg' in ds_name:
            input_prompt = base_prompt
        elif 'vqa' in ds_name:
            input_prompt = base_prompt
        else:
            input_prompt = base_prompt

        dataset = VQADataset(
            ds_name,
            input_prompt,
            args.few_shot,
            image_size,
            args.dynamic,
            use_thumbnail,
            args.max_num
        )
        dataloader = torch.utils.data.DataLoader(
            dataset=dataset,
            sampler=InferenceSampler(len(dataset)),
            batch_size=args.batch_size,
            num_workers=args.num_workers,
            pin_memory=True,
            drop_last=False,
            collate_fn=partial(collate_fn, tokenizer=tokenizer)
        )

        outputs = []
        for _, (pixel_values, questions, question_ids, annotations) in tqdm(enumerate(dataloader)):
            pixel_values = pixel_values.to(torch.bfloat16).cuda()
            generation_config = dict(
                num_beams=args.num_beams,
                min_new_tokens=1,
                do_sample=True if args.temperature > 0 else False,
                temperature=args.temperature,
                max_new_tokens=1200,
            )
            pred = model.chat(
                tokenizer=tokenizer,
                pixel_values=pixel_values,
                question=questions[0],
                generation_config=generation_config,
                verbose=True
            )
            answers = [pred]   

            for question, question_id, answer, annotation in zip(questions, question_ids, answers, annotations):
                outputs.append({
                    'question_id': question_id,
                    'question': question,
                    'answer': answer,
                    'annotation': annotation
                })
        
        torch.distributed.barrier()
        world_size = torch.distributed.get_world_size()
        merged_outputs = [None for _ in range(world_size)]
        torch.distributed.all_gather_object(merged_outputs, json.dumps(outputs))

        merged_outputs = [json.loads(_) for _ in merged_outputs]
        merged_outputs = [_ for _ in itertools.chain.from_iterable(merged_outputs)]

        if torch.distributed.get_rank() == 0:
            print(f'Evaluating {ds_name} ...')
            time_prefix = time.strftime('%y%m%d%H%M%S', time.localtime())
            results_file = f'{ds_name}_{time_prefix}.json'
            results_file = os.path.join(args.out_dir, results_file)
            json.dump(merged_outputs, open(results_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
            print('Results saved to {}'.format(results_file))  

            if ds_collections[ds_name]['metric'] == 'accuracy':
                accuracy = evaluate_exact_match_accuracy(merged_outputs)
                print(ds_name, {'accuracy': accuracy})
                summaries.append([ds_name, {'accuracy': accuracy}])
            elif ds_collections[ds_name]['metric'] == 'slvqa_gen_score':
                evaluator = SLVQANLGEvaluator()
                scores, total_scores = evaluator.eval_pred_list(merged_outputs)
                print(total_scores)
                for k, v in scores.items():
                    print(ds_name, {k: v})
                    summaries.append([ds_name, {k: v}])
        torch.distributed.barrier() 

    out_path = '_'.join(args.checkpoint.split('/')[-2:])
    writer = open(os.path.join(args.out_dir, f'{out_path}.txt'), 'a')
    print(f"write results to file {os.path.join(args.out_dir, f'{out_path}.txt')}")
    for summary in summaries:
        print(summary)
        writer.write(f'{summary}\n')
    writer.close()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--datasets", type=str, default="slvqa")
    parser.add_argument('--batch-size', type=int, default=1)
    parser.add_argument('--num-workers', type=int, default=1)
    parser.add_argument('--num-beams', type=int, default=5)
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--out-dir', type=str, default='xyz_caption_results')
    parser.add_argument('--few-shot', type=int, default=0)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--dynamic', action='store_true')
    parser.add_argument('--max-num', type=int, default=6)
    parser.add_argument('--load-in-8bit', action='store_true')
    parser.add_argument('--load-in-4bit', action='store_true')
    parser.add_argument('--auto', action='store_true')
    parser.add_argument('--language', type=str)
    args = parser.parse_args() 

    args.datasets = ["slvqa_caption_" + args.language.lower()]
    assert args.batch_size == 1, 'Only batch size 1 is supported'

    torch.distributed.init_process_group(
        backend='nccl',
        world_size=int(os.getenv('WORLD_SIZE', '1')),
        rank=int(os.getenv('RANK', '0')),
        timeout=datetime.timedelta(seconds=180000)
    )

    torch.cuda.set_device(int(os.getenv('LOCAL_RANK', 0)))

    model, tokenizer = load_model_and_tokenizer(args) 
    image_size = model.config.force_image_size or model.config.vision_config.image_size
    use_thumbnail = model.config.use_thumbnail

    total_params = sum(p.numel() for p in model.parameters()) / 1e9
    if total_params > 20 or args.dynamic:
        args.num_beams = 1
        print(f'[test] total_params: {total_params}B, use num_beams: {args.num_beams}')
    else:
        print(f'[test] total_params: {total_params}B')
    print(f'[test] image_size: {image_size}')
    print(f'[test] template: {model.config.template}')
    print(f'[test] dynamic_image_size: {args.dynamic}')
    print(f'[test] use_thumbnail: {use_thumbnail}')

    evaluate_chat_model()  
    
