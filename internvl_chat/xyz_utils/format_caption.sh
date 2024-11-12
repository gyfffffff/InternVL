image_save_path="/mnt/workspace/gaoyufei/xyz_v2_data"

# ar 270k
python xyz_utils/format_caption.py \
    --prompt_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_utils/prompt_for_caption.json \
    --language ar \
    --caption_json /mnt/workspace/gaoyufei/xyz_v2_data/trans_ar.json \
    --image_jsonl /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/ar/image_release_v2_ar_image_pure_json_in_part-671a21ac4ee0-000000.jsonl \
    --image_save_path ${image_save_path} \
    --save_path /mnt/workspace/gaoyufei/InternVL/internvl_chat/xyz_data/ar/ar_pure_caption_270k.jsonl \
    --data_length 100000