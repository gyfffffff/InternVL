import json
import os

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def merge_json_files(input_folder, output_file):
    merged_data = []
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(input_folder, file_name)
            data = read_json(file_path)
            merged_data.extend(data)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(merged_data, file, ensure_ascii=False, indent=4)

input_folder = '/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/xyz_data/hu'  # 替换为你的JSON文件所在的文件夹路径
output_file = '/nas/shared/ADLab_Oasim/gaoyufei/InternVL/internvl_chat/xyz_data/hu/trans_hu.json'  # 合并后的JSON文件名

merge_json_files(input_folder, output_file)