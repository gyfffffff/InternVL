# ar pair 1/4
# python src/data_prepare/download_json.py \
#     --language ar \
#     --image_type image_text_pair \
#     --jsonl_name v001_part-666c3ce73bf5-000000.jsonl \
#     --save_path /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/data \

# sr pair v001
# python xyz_utils/download_jsonl.py \
#     --language sr \
#     --image_type image_text_pair \
#     --jsonl_path image/release/sr/image_text_pair/json_in/part-67065fe92bdb-000000.jsonl\
#     --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data \

# ar v2
python xyz_utils/download_jsonl.py \
    --language ar \
    --image_type image_text_pair \
    --jsonl_path image/release_v2/ar/image_text_pair/json_in/part-671a196bab97-000000.jsonl \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data \


# vi v2
python xyz_utils/download_jsonl.py \
    --language vi \
    --image_type image_text_pair \
    --jsonl_path image/release_v2/vi/image_text_pair/json_in/part-671a1733cf93-000000.jsonl \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data \