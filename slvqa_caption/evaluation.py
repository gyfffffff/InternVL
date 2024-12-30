import json
import os
import random
import time
import os
from tqdm import tqdm
from torch.utils.data import DataLoader, Dataset
from inference import Qwen2VL
from slvqa_evaluator import SLVQANLGEvaluator


ds_collections = {
    'slvqa_caption_ar': {
        'test': 'data/SLVQA/AR/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },
    'slvqa_caption_hu': {
        'test': 'data/SLVQA/HU/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },    
    'slvqa_caption_vi': {
        'test': 'data/SLVQA/VI/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },
    'slvqa_caption_cs': {
        'test': 'data/SLVQA/CS/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },   
    'slvqa_caption_ko': {
        'test': 'data/SLVQA/KO/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },
    'slvqa_caption_th': {
        'test': 'data/SLVQA/TH/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },    
    'slvqa_caption_ru': {
        'test': 'data/SLVQA/RU/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    },
    'slvqa_caption_sr': {
        'test': 'data/SLVQA/SR/NLG/caption_test.jsonl',
        'metric': 'slvqa_gen_score',
    }
}




class VQADataset(Dataset):
    def __init__(self, ds_name):
        self.ds_name = ds_name

        # {"id": 0, "image": "/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/data/SLVQA/AR/images/0.jpg", "question": "وصف هذه الصورة.", "answer": "تُظهر هذه الصورة مشهدًا لشارع المدينة في يوم ثلجي. موضوع الصورة هو سيارة مغطاة بالثلوج الكثيفة، والسقف وغطاء المحرك مغطى بالثلج، والمساحات الموجودة على الزجاج الأمامي منحنية بسبب الثلج. وفي الجزء الخلفي من السيارة، يمكن رؤية امرأة ترتدي معطفا أخضر وهي تركب دراجة كهربائية ويبدو أنها تقود سيارتها في شارع مغطى بالثلوج. كانت المرأة ترتدي معطفًا أخضر ثقيلًا وقبعة، ويبدو أنها ترتديها للدفء. بدا تعبيرها هادئًا وركز على الطريق أمامها. ويمكن رؤية مركبات ومباني أخرى في الخلفية، وقد تساقطت عليها الثلوج أيضًا، مما يشير إلى تساقط الثلوج بكثافة. تنقل هذه الصورة أجواء الشتاء، ربما في منطقة تشهد تساقط الثلوج بغزارة. وتشير السيارة المغطاة بالثلوج وملابس المرأة إلى أن الطقس بارد، بينما يدل سلوك المرأة في الركوب في الثلج على أن الناس ما زالوا بحاجة للسفر في الطقس السيئ. تتناقض العناصر الموجودة في خلفية الصورة، مثل المركبات والمباني الأخرى، مع الموضوع، مما يسلط الضوء على تأثير الطقس الثلجي على الحياة الحضرية. كما تشير الشوارع والمركبات المغطاة بالثلوج إلى تأثير تساقط الثلوج على حركة المرور والحياة اليومية. هذه الصورة لا تظهر بشكل مباشر الخصائص الثقافية لبلد أو أمة معينة، ولكن من خلال الثلوج والملابس النسائية، يمكنك أن تشعر بأجواء الشتاء، والتي قد تكون مرتبطة بالعديد من البلدان أو المناطق التي تعيش فصل الشتاء. من الناحية العاطفية أو الجوية، قد تثير هذه الصورة مشاعر صفاء وجمال الشتاء، ولكنها قد تثير أيضًا أفكارًا حول إزعاجات وتحديات الطقس البارد. مشهد السيارة المغطاة بالثلوج والمرأة التي تركب في الثلج قد يذكر الناس بالهدوء والمرونة التي يتميز بها الشتاء."}

        with open(os.path.join("/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/" + ds_collections[ds_name]['test']), 'r') as f:
            self.data = [json.loads(line) for line in f]
    
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return self.data[idx]
    
def evaluate_chat_model(args):
    random.seed(2024)
    qwen2vl = Qwen2VL()

    for ds_name in args.datasets:
        dataset = VQADataset(ds_name)
        dataloader = DataLoader(
            dataset=dataset,
            batch_size=1,
            num_workers=2
        )

        outputs = []
        for _, item in tqdm(enumerate(dataloader)):
            image_path = item['image'][0]
            question = item['question'][0]
            question_id = item['id'].item()
            annotation = item['answer'][0]
            answer = qwen2vl.inference(image_path, question)
            print(question_id)
            print(answer)
            outputs.append({
                'question_id': question_id,
                'question': question,
                'answer': answer,
                'annotation': annotation
            })
            

        time_prefix = time.strftime('%y%m%d%H%M%S', time.localtime())
        results_file = f'{ds_name}_{time_prefix}.json'
        results_file = os.path.join(args.out_dir, results_file)
        json.dump(outputs, open(results_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
        print('Results saved to {}'.format(results_file))  

        evaluator = SLVQANLGEvaluator()
        scores, _ = evaluator.eval_pred_list(outputs)
        summaries = []
        for k, v in scores.items():
            summaries.append([ds_name, {k: v}])

        out_path = "qwen2vl" + "_" + args.language
        writer = open(os.path.join(args.out_dir, f'{out_path}.txt'), 'a')
        print(f"write results to file {os.path.join(args.out_dir, f'{out_path}.txt')}")
        for summary in summaries:
            # print(summary)
            writer.write(f'{summary}\n')
        writer.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasets', type=str, nargs='+')
    parser.add_argument('--language', type=str, default='ar')
    parser.add_argument('--out_dir', type=str, default='xyz_caption_results')
    args = parser.parse_args()

    args.datasets = ['slvqa_caption_'+args.language]
    evaluate_chat_model(args)