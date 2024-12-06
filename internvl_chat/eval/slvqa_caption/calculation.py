from slvqa_evaluator import SLVQANLGEvaluator

# ds_collections = {
#     'slvqa_caption_ar': {
#         'test': 'data/SLVQA/AR/NLG/caption_test.jsonl',
#         'metric': 'slvqa_gen_score',
#     },
#     'slvqa_caption_hu': {
#         'test': 'data/SLVQA/HU/NLG/caption_test.jsonl',
#         'metric': 'slvqa_gen_score',
#     },    
# }

if __name__ == '__main__':
    import argparse
    import os
    import json
    from tqdm import tqdm
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', type=str)
    parser.add_argument('--checkpoint', type=str)
    parser.add_argument('--results_file', type=str)
    parser.add_argument('--out-dir', type=str, default='xyz_caption_results')
    args = parser.parse_args() 

    ds_name = f'slvqa_caption_{args.language}'

    with open(args.results_file, 'r') as f:
        merged_outputs = json.load(f)

    evaluator = SLVQANLGEvaluator()
    scores, total_scores = evaluator.eval_pred_list(merged_outputs)
    print(total_scores)
    summaries = []
    for k, v in scores.items():
        print(ds_name, {k: v})
        summaries.append([ds_name, {k: v}])

    out_path = '_'.join(args.checkpoint.split('/')[-2:]) + "_"+args.language
    writer = open(os.path.join(args.out_dir, f'{out_path}.txt'), 'a')
    print(f"write results to file {os.path.join(args.out_dir, f'{out_path}.txt')}")
    for summary in summaries:
        # print(summary)
        writer.write(f'{summary}\n')
    writer.close()

