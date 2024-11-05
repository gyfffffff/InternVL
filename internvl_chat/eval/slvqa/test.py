def compute_bleu_score(self, pred_answer, gt_answer):
    from nltk.translate.bleu_score import sentence_bleu
    return sentence_bleu([gt_answer.split()], pred_answer.split())

def compute_meteor_score(self, pred_answer, gt_answer):
    from nltk.translate.meteor_score import meteor_score
    print(f"pred_answer: {pred_answer}, gt_answer: {gt_answer}")
    return meteor_score([gt_answer.split()], pred_answer.split())

def compute_rouge_score(self, pred_answer, gt_answer):
    from rouge import Rouge
    rouger = Rouge()
    scores = rouger.get_scores(pred_answer, gt_answer)
    return scores[0]['rouge-l']['f']

def compute_spice_cider_score(self, pred_answer, gt_answer):
    from aac_metrics import evaluate
    corpus_scores, _ = evaluate([pred_answer, pred_answer], [[gt_answer], [gt_answer]])
    return corpus_scores['spice'], corpus_scores['cider_d']


if __name__ == '__main__':
    pred_answer = "this image shows 2 men in traditional middle eastern attire squatting and planting small tree"
    gt_answer = "d"
    # bleu_score = compute_bleu_score(None, pred_answer, gt_answer)
    # print(bleu_score)
    # meteor_score = compute_meteor_score(None, pred_answer, gt_answer)
    # print(meteor_score)
    # rouge_score = compute_rouge_score(None, pred_answer, gt_answer)
    # print(rouge_score)
    spice_score = compute_spice_score(None, pred_answer, gt_answer)
    print(spice_score)
    cider_score = compute_cider_score(None, pred_answer, gt_answer)
    print(cider_score)



