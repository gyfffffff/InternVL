# sr v001
# jsonl_name="image_pre_process_0930_sr_v001_image_text_pair_image_text_pair.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/sr/${jsonl_name} \
#     --language sr \
#     --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
#     --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/sr/preprocessed_${jsonl_name} \
#     --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/sr/image_text_pair_save.txt \
#     --version v001 \


image_save_path="/mnt/workspace/gaoyufei/xyz_v2_data"

# ar v2
jsonl_name="image_release_v2_ar_image_text_pair_json_in_part-671a196bab97-000000.jsonl"
data_length=75000
python xyz_utils/format.py \
    --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/ar/${jsonl_name} \
    --language ar \
    --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/ar/preprocessed_newprompt_${data_length}_${jsonl_name} \
    --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/ar/image_text_pair_save.txt \
    --version  "" \
    --image_save_path ${image_save_path} \
    --data_length ${data_length}

# # vi v2
jsonl_name="image_release_v2_vi_image_text_pair_json_in_part-671a1733cf93-000000.jsonl"
data_length=75000
python xyz_utils/format.py \
    --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/${jsonl_name} \
    --language vi \
    --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/preprocessed_${data_length}_${jsonl_name} \
    --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/image_text_pair_save.txt \
    --version  "" \
    --image_save_path ${image_save_path} \
    --data_length ${data_length}

jsonl_name="image_release_v2_vi_image_text_pair_json_in_part-671a1733cf93-000000.jsonl"
data_length=50000
python xyz_utils/format.py \
    --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/${jsonl_name} \
    --language vi \
    --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/preprocessed_${data_length}_${jsonl_name} \
    --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/image_text_pair_save.txt \
    --version  "" \
    --image_save_path ${image_save_path} \
    --data_length ${data_length}

jsonl_name="image_release_v2_vi_image_text_pair_json_in_part-671a1733cf93-000000.jsonl"
data_length=100000
python xyz_utils/format.py \
    --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/${jsonl_name} \
    --language vi \
    --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/preprocessed_${data_length}_${jsonl_name} \
    --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/vi/image_text_pair_save.txt \
    --version  "" \
    --image_save_path ${image_save_path} \
    --data_length ${data_length}


# test
# jsonl_name="image_text_pair.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/test/${jsonl_name} \
#     --language ar \
#     --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt.json \
#     --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/test/preprocessed_${jsonl_name} \
#     --image_safe_file /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/test/image_text_pair_save.txt \
#     --version  "" \
#     --image_save_path ${image_save_path} \
