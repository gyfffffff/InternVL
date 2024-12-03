import json

def calculate_average_length_of_gt(gt_file_path):
    with open(gt_file_path, 'r') as f:
        data = f.readlines()
        json_data = [json.loads(line) for line in data]
        length = [len(json_data['answer']) for json_data in json_data]
    print(f'Average length of GT: {sum(length)/len(length)}')

if __name__ == '__main__':
    language = 'HU'
    gt_file_path = f'data/SLVQA/{language}/NLG/caption_test.jsonl'
    calculate_average_length_of_gt(gt_file_path)
