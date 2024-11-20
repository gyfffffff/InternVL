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
    caption_json = args.caption_json
    image_jsonl = args.image_jsonl
    image_save_path = args.image_save_path
    image_type = 'image_pure'
    language = args.language
    save_path = args.save_path
    prompt_path = args.prompt_path
    prompt_randomseed = args.prompt_randomseed
    data_length = args.data_length

    caption_data = json.loads(open(caption_json, 'r').read())
    caption_dict = {}
    for caption in caption_data:
        caption_dict[caption['img_id']] = caption['caption']
    with open(image_jsonl, 'r') as f:
        raw_data = [json.loads(line) for line in f.readlines()]
    data_num = 0
    for i, data in enumerate(raw_data):
        if data_num > data_length:
            break
        data_item = {}
        data_item['id'] = i
        img_name = data['image']['path'].split('/')[-1].split('.')[0]
        data_item['image'] = f'{image_save_path}/{language}/{image_type}/{img_name}'
        import pdb; pdb.set_trace()
        if os.path.exists(data_item['image']) == False:
            continue
        data_item['width'] = data['image']['resolution'][0]
        data_item['height'] = data['image']['resolution'][1]
        conversations = []
        prompt, sample_id = sample_prompt(prompt_path, prompt_randomseed, language)
        conversation_human = {
            'from': 'human',
            'value': f"<image>\n{prompt}",
            'prompt_sample_id': sample_id
        }
        try:
            import pdb; pdb.set_trace()
            conversation_gpt = {
                'from': 'gpt',
                'value': caption_dict[img_name]
            }
        except:
            continue
        conversations.append(conversation_human)
        conversations.append(conversation_gpt)
        data_item['conversations'] = conversations

        with open(save_path, 'a+') as f:
            f.write(json.dumps(data_item, ensure_ascii=False))
            f.write('\n')
        data_num += 1
    return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt_path', type=str)
    parser.add_argument('--prompt_randomseed', type=int, default=0)
    parser.add_argument('--language', type=str)
    parser.add_argument('--caption_json', type=str)
    parser.add_argument('--image_jsonl', type=str)
    parser.add_argument('--image_save_path', type=str)
    parser.add_argument('--save_path', type=str)
    parser.add_argument('--data_length', type=int)
    args = parser.parse_args()

    format(args)    
