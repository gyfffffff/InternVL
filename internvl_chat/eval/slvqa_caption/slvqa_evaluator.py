from tqdm import tqdm
import re


class EvalAIAnswerProcessor:
    """
    Processes an answer similar to Eval AI
        copied from
        https://github.com/facebookresearch/mmf/blob/c46b3b3391275b4181567db80943473a89ab98ab/pythia/tasks/processors.py#L897
    """

    CONTRACTIONS = {
        'aint': "ain't",
        'arent': "aren't",
        'cant': "can't",
        'couldve': "could've",
        'couldnt': "couldn't",
        "couldn'tve": "couldn't've",
        "couldnt've": "couldn't've",
        'didnt': "didn't",
        'doesnt': "doesn't",
        'dont': "don't",
        'hadnt': "hadn't",
        "hadnt've": "hadn't've",
        "hadn'tve": "hadn't've",
        'hasnt': "hasn't",
        'havent': "haven't",
        'hed': "he'd",
        "hed've": "he'd've",
        "he'dve": "he'd've",
        'hes': "he's",
        'howd': "how'd",
        'howll': "how'll",
        'hows': "how's",
        "Id've": "I'd've",
        "I'dve": "I'd've",
        'Im': "I'm",
        'Ive': "I've",
        'isnt': "isn't",
        'itd': "it'd",
        "itd've": "it'd've",
        "it'dve": "it'd've",
        'itll': "it'll",
        "let's": "let's",
        'maam': "ma'am",
        'mightnt': "mightn't",
        "mightnt've": "mightn't've",
        "mightn'tve": "mightn't've",
        'mightve': "might've",
        'mustnt': "mustn't",
        'mustve': "must've",
        'neednt': "needn't",
        'notve': "not've",
        'oclock': "o'clock",
        'oughtnt': "oughtn't",
        "ow's'at": "'ow's'at",
        "'ows'at": "'ow's'at",
        "'ow'sat": "'ow's'at",
        'shant': "shan't",
        "shed've": "she'd've",
        "she'dve": "she'd've",
        "she's": "she's",
        'shouldve': "should've",
        'shouldnt': "shouldn't",
        "shouldnt've": "shouldn't've",
        "shouldn'tve": "shouldn't've",
        "somebody'd": 'somebodyd',
        "somebodyd've": "somebody'd've",
        "somebody'dve": "somebody'd've",
        'somebodyll': "somebody'll",
        'somebodys': "somebody's",
        'someoned': "someone'd",
        "someoned've": "someone'd've",
        "someone'dve": "someone'd've",
        'someonell': "someone'll",
        'someones': "someone's",
        'somethingd': "something'd",
        "somethingd've": "something'd've",
        "something'dve": "something'd've",
        'somethingll': "something'll",
        'thats': "that's",
        'thered': "there'd",
        "thered've": "there'd've",
        "there'dve": "there'd've",
        'therere': "there're",
        'theres': "there's",
        'theyd': "they'd",
        "theyd've": "they'd've",
        "they'dve": "they'd've",
        'theyll': "they'll",
        'theyre': "they're",
        'theyve': "they've",
        'twas': "'twas",
        'wasnt': "wasn't",
        "wed've": "we'd've",
        "we'dve": "we'd've",
        'weve': "we've",
        'werent': "weren't",
        'whatll': "what'll",
        'whatre': "what're",
        'whats': "what's",
        'whatve': "what've",
        'whens': "when's",
        'whered': "where'd",
        'wheres': "where's",
        'whereve': "where've",
        'whod': "who'd",
        "whod've": "who'd've",
        "who'dve": "who'd've",
        'wholl': "who'll",
        'whos': "who's",
        'whove': "who've",
        'whyll': "why'll",
        'whyre': "why're",
        'whys': "why's",
        'wont': "won't",
        'wouldve': "would've",
        'wouldnt': "wouldn't",
        "wouldnt've": "wouldn't've",
        "wouldn'tve": "wouldn't've",
        'yall': "y'all",
        "yall'll": "y'all'll",
        "y'allll": "y'all'll",
        "yall'd've": "y'all'd've",
        "y'alld've": "y'all'd've",
        "y'all'dve": "y'all'd've",
        'youd': "you'd",
        "youd've": "you'd've",
        "you'dve": "you'd've",
        'youll': "you'll",
        'youre': "you're",
        'youve': "you've",
    }

    NUMBER_MAP = {
        'none': '0',
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
    }
    ARTICLES = ['a', 'an', 'the']
    PERIOD_STRIP = re.compile(r'(?!<=\d)(\.)(?!\d)')
    COMMA_STRIP = re.compile(r'(?<=\d)(\,)+(?=\d)')
    PUNCTUATIONS = [
        ';',
        r'/',
        '[',
        ']',
        '"',
        '{',
        '}',
        '(',
        ')',
        '=',
        '+',
        '\\',
        '_',
        '-',
        '>',
        '<',
        '@',
        '`',
        ',',
        '?',
        '!',
    ]

    def __init__(self, *args, **kwargs):
        pass

    def word_tokenize(self, word):
        word = word.lower()
        word = word.replace(',', '').replace('?', '').replace("'s", " 's")
        return word.strip()

    def process_punctuation(self, in_text):
        out_text = in_text
        for p in self.PUNCTUATIONS:
            if (p + ' ' in in_text or ' ' + p in in_text) or (
                re.search(self.COMMA_STRIP, in_text) is not None
            ):
                out_text = out_text.replace(p, '')
            else:
                out_text = out_text.replace(p, ' ')
        out_text = self.PERIOD_STRIP.sub('', out_text, re.UNICODE)
        return out_text

    def process_digit_article(self, in_text):
        out_text = []
        temp_text = in_text.lower().split()
        for word in temp_text:
            word = self.NUMBER_MAP.setdefault(word, word)
            if word not in self.ARTICLES:
                out_text.append(word)
            else:
                pass
        for word_id, word in enumerate(out_text):
            if word in self.CONTRACTIONS:
                out_text[word_id] = self.CONTRACTIONS[word]
        out_text = ' '.join(out_text)
        return out_text
    
    def trucate(self, item):
        max_len = 1300
        print(213, len(item))
        if len(item) > max_len:
            item = item[:max_len]
        return item

    def __call__(self, item):
        item = self.word_tokenize(item)
        item = item.replace('\n', ' ').replace('\t', ' ').strip()
        item = self.process_punctuation(item)
        item = self.process_digit_article(item)
        item = self.trucate(item)
        return item




class SLVQANLGEvaluator:
    def __init__(self):
        self.answer_processor = EvalAIAnswerProcessor()

    def _compute_answer_scores(self, answers):
        """
        compute the accuracy (soft score) of human answers
        """
        answers = [self.answer_processor(a) for a in raw_answers]
        assert len(answers) == 10
        gt_answers = list(enumerate(answers))
        unique_answers = set(answers)
        unique_answer_scores = {}

        for unique_answer in unique_answers:
            accs = []
            for gt_answer in gt_answers:
                other_answers = [item for item in gt_answers if item != gt_answer]
                matching_answers = [
                    item for item in other_answers if item[1] == unique_answer
                ]
                acc = min(1, float(len(matching_answers)) / 3)
                accs.append(acc)
            unique_answer_scores[unique_answer] = sum(accs) / len(accs)

        return unique_answer_scores       

        
    def compute_score(self, pred_answer, gt_answer):
        from aac_metrics import evaluate
        corpus_scores, _ = evaluate([pred_answer, pred_answer], [[gt_answer], [gt_answer]])
        return corpus_scores


    def eval_pred_list(self, pred_list):
        # slvqa_gen_score:
        # - B-1 (BLEU-1)
        # - M (METEOR)
        # - R (ROUGE-L)
        # - S (SPICE)
        # - C (CIDEr)

        # pred_list:
        # [{"question_id": , "question": "", "answer": "", "annotation": ""}, {...}, ...]
        scores = {}
        for entry in tqdm(pred_list):
            pred_answer = self.answer_processor(entry["answer"])
            gt_answer = entry['annotation']
            if len(gt_answer) > 1300:
                gt_answer = gt_answer[:1300]
            question_id = entry['question_id']
            try:
                computed_scores = self.compute_score(pred_answer, gt_answer)
                print(computed_scores)
                for k, v in computed_scores.items():
                    scores[k] = scores.get(k, [])
                    scores[k].append(v)
            except Exception as e:
                print(e)
                pass
        print(275, scores)
        average_scores = {}
        for metric in scores.keys():
            average_scores[metric] = sum(scores[metric]) / len(scores[metric])

        return average_scores, scores

