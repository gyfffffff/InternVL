import argparse
import os
import re

import torch
from internvl.model import load_model_and_tokenizer
from internvl.train.dataset import build_transform, dynamic_preprocess
from PIL import Image
from tqdm import tqdm

import json


def load_image(image_file, input_size=224):
    image = Image.open(image_file).convert('RGB')
    transform = build_transform(is_train=False, input_size=input_size)
    if args.dynamic:
        images = dynamic_preprocess(image, image_size=input_size,
                                    use_thumbnail=use_thumbnail,
                                    max_num=args.max_num)
    else:
        images = [image]
    pixel_values = [transform(image) for image in images]
    pixel_values = torch.stack(pixel_values)
    return pixel_values


def post_processing(response):
    response = response.replace('\n', '').replace('不是', 'No').replace('是', 'Yes').replace('否', 'No')
    response = response.lower().replace('true', 'yes').replace('false', 'no')
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    response = re.sub(pattern, '', response)
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', type=str, default='')
    parser.add_argument('--language', type=str, default='EN')
    parser.add_argument('--root', type=str, default='./data/SLVQA')
    parser.add_argument('--num-beams', type=int, default=5)
    parser.add_argument('--top-k', type=int, default=50)
    parser.add_argument('--top-p', type=float, default=0.9)
    parser.add_argument('--sample', type=bool, default=False)
    parser.add_argument('--dynamic', action='store_true')
    parser.add_argument('--max-num', type=int, default=6)
    parser.add_argument('--load-in-8bit', action='store_true')
    parser.add_argument('--load-in-4bit', action='store_true')
    parser.add_argument('--auto', action='store_true')
    args = parser.parse_args()

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
    print(f'[test] max_num: {args.max_num}')

    output = f"xyz_caption_result/{args.language}/{args.language}_{checkpoint.replace('//', '_')}.jsonl"

    prompt = {"EN": 'Answer the question using a single word or phrase.',
    "AR": 'أجب على السؤال باستخدام كلمة واحدة أو عبارة واحدة.',
    "CS": 'Odpovězte na otázku pomocí jediného slova nebo fráze.',
    "SR": 'Одговорите на питање користећи једну реч или фразу.',
    "HU": 'Válaszoljon a kérdésre egyetlen szó vagy kifejezés használatával.',}

    with open(os.path.join(args.root, args.language, "anns.jsonl"), 'r') as f:
        lines = f.readlines()
    # print(lines[:5])
    # {"image_id": "354_realworldqa_44.webp", "question": "أين يقع هذا السنجاب بالنسبة إلى النافذة؟  أ. السنجاب ليس قريبًا من النافذة.  ب. السنجاب قريب من النافذة ينظر إلى الداخل.  ج. السنجاب بعيد عن النافذة.  يرجى الإجابة مباشرة بحرف الخيار الصحيح فقط ولا شيء آخر.", "answer": "B"}
    for line in lines:
        # print(line)
        content = json.loads(line)
        img, question, gt = content['image_id'], content['question'], content['answer']
        question = question + ' ' + prompt[args.language]
        img_path = os.path.join('./data/SLVQA/EN/images', img)
        assert os.path.exists(img_path), img_path
        
        pixel_values = load_image(img_path, image_size).cuda().to(torch.bfloat16)
        generation_config = dict(
            do_sample=args.sample,
            top_k=args.top_k,
            top_p=args.top_p,
            num_beams=args.num_beams,
            max_new_tokens=20,
            eos_token_id=tokenizer.eos_token_id,
        )
        response = model.chat(
            tokenizer=tokenizer,
            pixel_values=pixel_values,
            question=question,
            generation_config=generation_config,
            verbose=True
        )
        response = post_processing(response)
        with open(output, 'a+', encoding='utf-8') as f:
            f.write('\t'.join([img, question, gt, response]) + '\n')

