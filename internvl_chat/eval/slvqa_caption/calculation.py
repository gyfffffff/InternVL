import argparse
import os

from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score,
                             recall_score)

parser = argparse.ArgumentParser()
parser.add_argument('--results_dir', default='./LaVIN', type=str)
parser.add_argument('--language', default='EN', type=str)

eval_type_dict = {
    'Perception': ['existence', 'count', 'position', 'color', 'posters', 'celebrity', 'scene', 'landmark', 'artwork', 'OCR'],
    'Cognition': ['commonsense_reasoning', 'numerical_calculation', 'text_translation', 'code_reasoning']
}


class calculate_metrics:
    def divide_chunks(self, l, n=2):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]

        return

    def parse_pred_ans(self, pred_ans):
        pred_label = None
        if pred_ans in ['yes', 'no']:
            pred_label = pred_ans
        else:
            prefix_pred_ans = pred_ans[:4]

            if 'yes' in prefix_pred_ans:
                pred_label = 'yes'
            elif 'no' in prefix_pred_ans:
                pred_label = 'no'
            else:
                pred_label = 'other'

        return pred_label

    def compute_metric(self, gts, preds):
        assert len(gts) == len(preds)

        yes = 'نعم'
        no = 'لا يوجد'
        tp = 0
        fn = 0
        tn = 0
        fp = 0
        other_num = 0
        for gt, pred in zip(gts, preds):
            # import pdb; pdb.set_trace() 
            if gt == yes and pred == yes:
                tp += 1
            elif gt == yes and pred == no:
                fn += 1
            elif gt == no and pred == yes:
                fp += 1
            elif gt == no and pred == no:
                tn += 1
            else:
                other_num += 1
        precision = tp / (tp + fp) if tp + fp != 0 else 0
        recall = tp / (tp + fn) if tp + fn != 0 else 0
        other_num = other_num / len(gts)
        acc = accuracy_score(gts, preds)

        metric_dict = dict()
        metric_dict = {
            'TP': tp,
            'FN': fn,
            'TN': tn,
            'FP': fp,
            'precision': precision,
            'recall': recall,
            'other_num': other_num,
            'acc': acc,
        }

        return metric_dict

    def process_result(self, results_dir, language):

        model_score_dict = dict()
        with open(os.path.join(results_dir, language+".jsonl"), 'r') as f:
            res_lines = f.readlines()

        result_dict = {}
        for line in res_lines:
            # 1_mme_color_000000006723.jpg	هل يوجد مبنى من الطوب الأحمر في الصورة؟ الرجاء الإجابة بنعم أو لا. أجب على السؤال باستخدام كلمة واحدة أو عبارة واحدة.	نعم	نعم.
            img_name, question, gt_ans, pred_ans = line.strip().split('\t')
            splited = img_name.split('_')
            if len(splited) == 4:
                dataset = img_name.split('_')[1]+"_"+img_name.split('_')[2]
            else:
                dataset = img_name.split('_')[1]
            result_dict[dataset] = result_dict.get(dataset, [])
            result_dict[dataset].append((gt_ans, pred_ans[:len(gt_ans)]))

        with open(os.path.join(results_dir, language+".txt"), 'a') as f:
            for dataset, res_list in result_dict.items():
                gts = [res[0] for res in res_list]
                preds = [res[1] for res in res_list]
                metric_dict = self.compute_metric(gts, preds)
                img_num = len(gts)
                print('dataset:', dataset)
                f.write(f"{dataset}\n")
                for k, v in metric_dict.items():
                    print('\t', k, ':', v)
                    f.write(f"\t{k}: {v}\n")


            

        # for eval_type, task_name_list in eval_type_dict.items():
        #     print('===========', eval_type, '===========')

        #     scores = 0
        #     task_score_dict = dict()

        #     for task_name in task_name_list:

        #         task_txt = os.path.join(results_dir, task_name + '.txt')
        #         lines = open(task_txt, 'r').readlines()
        #         chunk_lines = list(self.divide_chunks(lines)) # one image corresponds to two questions

        #         img_num = len(chunk_lines)
        #         task_other_ans_num = 0
        #         task_score = 0
        #         acc_plus_correct_num = 0
        #         gts = []
        #         preds = []

        #         for img_items in chunk_lines:
        #             assert len(img_items) == 2
        #             img_correct_num = 0

        #             for img_item in img_items:
        #                 try:
        #                     img_name, question, gt_ans, pred_ans = img_item.split('\t')
        #                 except:
        #                     print(img_item)
        #                     continue
        #                 gt_ans = gt_ans.lower()
        #                 pred_ans = pred_ans.lower()

        #                 assert gt_ans in ['yes', 'no'] # gt can only be yes or no.

        #                 pred_ans = self.parse_pred_ans(pred_ans)
        #                 assert pred_ans in ['yes', 'no', 'other']

        #                 gts.append(gt_ans)
        #                 preds.append(pred_ans)

        #                 if gt_ans == pred_ans:
        #                     img_correct_num += 1

        #                 if pred_ans not in ['yes', 'no']:
        #                     task_other_ans_num += 1

        #             if img_correct_num == 2:
        #                 acc_plus_correct_num += 1

        #         # cal TP precision acc, etc.
        #         metric_dict = self.compute_metric(gts, preds)
        #         acc_plus = acc_plus_correct_num / img_num
        #         metric_dict['acc_plus'] = acc_plus

        #         for k, v in metric_dict.items():
        #             if k in ['acc', 'acc_plus']:
        #                 task_score += v*100

        #         task_score_dict[task_name] = task_score

        #         scores += task_score

        #     print('total score:', scores, '\n')
        #     for task_name, score in task_score_dict.items():
        #         print('\t', task_name, ' score:', score)
        #     print('\n')

        # return


if __name__ == '__main__':
    cal = calculate_metrics()

    args = parser.parse_args()
    results_dir = args.results_dir
    cal.process_result(results_dir, args.language)
