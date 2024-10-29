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
from textvqa_eval import TextVQAAccuracyEvaluator
from tqdm import tqdm

ds_collections = {
    'slvqa_choice': {
        'test': 'data/slvqa/test.jsonl',
        'metric': 'accuracy',
    },
    'slvqa_gen': {
        'test': 'data/slvqa/test.jsonl',
        'metric': 'slvqa_gen_score',
    }
}


def evaluate_chat_model():
    random.seed(args.seed)
    summaries = []

    dataset = VQADataset(
        args.dataset
    )
    dataloader = torch.utils.data.DataLoader(
        dataset=dataset,
        batch_size=args.batch_size
    )
    outputs = []

    for ds_name in args.datasets:
        for _, (pixel_values, questions, question_ids, annotations) in tqdm(enumerate(dataloader)):
            pixel_values = pixel_values.to(torch.bfloat16).cuda()
            generation_config = dict(
                num_beams=args.num_beams,
                max_new_tokens=ds_collections[ds_name]['max_new_tokens'],
                min_new_tokens=1,
                do_sample=True if args.temperature > 0 else False,
                temperature=args.temperature,
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
            json.dump(merged_outputs, open(results_file, 'w'))
            print('Results saved to {}'.format(results_file))  

            if ds_collections[ds_name]['metric'] == 'accuracy':
                accuracy = evaluate_accuracy(merged_outputs)
                print(ds_name, {'accuracy': accuracy})
                summaries.append([ds_name, {'accuracy': accuracy}])
            elif ds_collections[ds_name]['metric'] == 'slvqa_gen_score':
                scores = get_slvqa_gen_score(merged_outputs)
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
    parser.add_argument("--dataset", type=str, default="slvqa")
    parser.add_argument('--batch-size', type=int, default=1)
    parser.add_argument('--num-workers', type=int, default=1)
    parser.add_argument('--num-beams', type=int, default=5)
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--out-dir', type=str, default='xyz_results')
    parser.add_argument('--few-shot', type=int, default=0)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--dynamic', action='store_true')
    # parser.add_argument('--max-num', type=int, default=6)
    # parser.add_argument('--load-in-8bit', action='store_true')
    # parser.add_argument('--load-in-4bit', action='store_true')
    parser.add_argument('--auto', action='store_true')
    args = parser.parse_args() 

    print('datasets:', args.datasets)

    torch.distributed.init_process_group(
        backend='nccl',
        world_size=int(os.getenv('WORLD_SIZE', '1')),
        rank=int(os.getenv('RANK', '0')),
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
    
