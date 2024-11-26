image_save_path="/nas/shared/ADLab_Oasim/gaoyufei/xyz_v2_data"
# ar 170k
save_path="xyz_data/ar/ar_combine_170k.jsonl"
python xyz_utils/format_caption.py \
    --prompt_path xyz_utils/prompt_for_caption.json \
    --language ar \
    --caption_json xyz_data/ar/trans_ar.json \
    --image_jsonl xyz_data/ar/image_release_v2_ar_image_pure_json_in_part-671a21ac4ee0-000000.jsonl \
    --image_save_path ${image_save_path} \
    --save_path  ${save_path}\
    --data_length 80000
jsonl_name="image_release_v2_ar_image_text_pair_json_in_part-671a196bab97-000000.jsonl"
python xyz_utils/format.py \
    --image_jsonl xyz_data/ar/${jsonl_name} \
    --language ar \
    --prompt_path xyz_utils/prompt.json \
    --save_path ${save_path} \
    --image_save_path ${image_save_path} \
    --data_length 90000