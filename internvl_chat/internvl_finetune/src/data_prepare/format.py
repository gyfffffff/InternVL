'''
{
  "id": 0,
  "image": "images/00000000.jpg",
  "width": 897,
  "height": 1152,
  "conversations": [
    {
      "from": "human",
      "value": "<image>\nCan you extract any readable text from the image?"
    },
    {
      "from": "gpt",
      "value": "Dares Wins Vol. 5 Tommy's Heroes Vol. 6: For Tomorrow Vol. 7: Closing Time miniseries. Clark Kent is being interviewed about Superman's connection to notorious killer Tommy Monaghan. Taking the conversation..."
    }
  ]
}
'''


'''
{"img_id":"774d57a9f8fe72a5c6fa01f6a0f2d3dc901b8a5e86e764de6880558f11484f95","url":"http://arabic.news.cn/2018-06/04/c_137228407_2.htm","data_source":"multi-web-news","image":{"path":"774d57a9f8fe72a5c6fa01f6a0f2d3dc901b8a5e86e764de6880558f11484f95","resolution":[899,599],"size":66.80078125,"format":"JPEG"},"captions":{"content":"الصورة: \"رقصة الدراويش\" خلال شهر رمضان في القاهرة","lang":"ar"},"labels":{"pjwk_cates":{"level1":["文化类"],"level2":["民俗传统"]}}}
'''


import argparse
import json
import random
import os

def sample_prompt(prompt_path, prompt_randomseed, language):
    with open(prompt_path, 'r') as f:
        prompts = json.loads(f.read())
    sample_id = random.randint(0, len(prompts['prompts']) - 1)
    prompt = prompts['prompts'][sample_id]["prompt"]
    return prompt[language], sample_id


def format(args):
    data_root_path = args.data_root_path
    save_root = args.save_root
    raw_jsonl_path = args.raw_jsonl_path
    language = args.language
    image_type = args.image_type
    prompt_randomseed = args.prompt_randomseed
    prompt_path = args.prompt_path

    with open(raw_jsonl_path, 'r') as f:
        raw_data = [json.loads(line) for line in f.readlines()]

    for i, data in enumerate(raw_data):
        data_item = {}
        data_item['id'] = i
        img_name = data['image']['path']
        img_format = data['image']['format'].lower()
        data_item['image'] = f'{data_root_path}/{language}/{image_type}/{img_name}.{img_format}'
        data_item['width'] = data['image']['resolution'][0] 
        data_item['height'] = data['image']['resolution'][1]
        conversations = []
        prompt, sample_id = sample_prompt(prompt_path, prompt_randomseed, language)
        conversation_human = {
            'from': 'human',
            'value': f"<image>\n{prompt}",
            'prompt_sample_id': sample_id
        }
        conversation_gpt = {
            'from': 'gpt',
            'value': data['captions']['content']
        }
        conversations.append(conversation_human)
        conversations.append(conversation_gpt)
        data_item['conversations'] = conversations

        save_path = f'{save_root}/{language}/{image_type}/processed/processed_{raw_jsonl_path.split("/")[-1].split(".")[0]}.jsonl'
        os.makedirs(f'{save_root}/{language}/{image_type}/processed', exist_ok=True)
        with open(save_path, 'a+') as f:
            f.write(json.dumps(data_item, ensure_ascii=False))
            f.write('\n')
    return 

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--data_root_path', type=str)
    argparser.add_argument('--save_root', type=str)
    argparser.add_argument('--raw_jsonl_path', type=str)
    argparser.add_argument('--language', type=str)
    argparser.add_argument('--image_type', type=str)
    argparser.add_argument('--prompt_randomseed', type=int, default=2024)
    argparser.add_argument('--prompt_path', type=str)
    args = argparser.parse_args()


    format(args)



