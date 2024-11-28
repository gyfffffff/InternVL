image_save_path="/nas/shared/ADLab_Oasim/gaoyufei/xyz_v2_data"
# th 
# save_path="xyz_data/th/th_caption_90k.jsonl"
# python xyz_utils/format_caption.py \
#     --prompt_path xyz_utils/prompt_for_caption.json \
#     --language th \
#     --caption_json xyz_data/th/trans_th.json \
#     --image_jsonl xyz_data/th/image_release_v2_th_image_pure_json_in_part-671b228af112-000000.jsonl \
#     --image_save_path ${image_save_path} \
#     --save_path  ${save_path}\
#     --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name="image_release_v2_th_image_text_pair_json_in_part-671b2319346b-000000.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/th/${jsonl_name} \
#     --language th \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

# language="vi"
# save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
# python xyz_utils/format_caption.py \
#     --prompt_path xyz_utils/prompt_for_caption.json \
#     --language ${language} \
#     --caption_json xyz_data/${language}/trans_${language}.json \
#     --image_jsonl  \
#     --image_save_path ${image_save_path} \
#     --save_path  ${save_path}\
#     --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name=""
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

# language="ko"
# save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
# python xyz_utils/format_caption.py \
#     --prompt_path xyz_utils/prompt_for_caption.json \
#     --language ${language} \
#     --caption_json xyz_data/${language}/trans_${language}.json \
#     --image_jsonl  \
#     --image_save_path ${image_save_path} \
#     --save_path  ${save_path}\
#     --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name=""
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

language="cs"
save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
python xyz_utils/format_caption.py \
    --prompt_path xyz_utils/prompt_for_caption.json \
    --language ${language} \
    --caption_json xyz_data/${language}/trans_${language}.json \
    --image_jsonl xyz_data/cs/image_release_v2_cs_image_pure_json_in_part-671b4dc72354-000000.jsonl \
    --image_save_path ${image_save_path} \
    --save_path  ${save_path}\
    --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name="image_release_v2_cs_image_text_pair_json_in_part-671b4e4002a4-000000.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

language="hu"
save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
python xyz_utils/format_caption.py \
    --prompt_path xyz_utils/prompt_for_caption.json \
    --language ${language} \
    --caption_json xyz_data/${language}/trans_${language}.json \
    --image_jsonl xyz_data/hu/image_release_v2_hu_image_pure_json_in_part-671a14965531-000000.jsonl \
    --image_save_path ${image_save_path} \
    --save_path  ${save_path}\
    --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name="image_release_v2_hu_image_text_pair_json_in_part-671a1822a82d-000000.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

language="sr"
save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
python xyz_utils/format_caption.py \
    --prompt_path xyz_utils/prompt_for_caption.json \
    --language ${language} \
    --caption_json xyz_data/${language}/trans_${language}.json \
    --image_jsonl xyz_data/sr/image_release_v2_sr_image_pure_json_in_part-671b3d7f8b44-000000.jsonl \
    --image_save_path ${image_save_path} \
    --save_path  ${save_path}\
    --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name="image_release_v2_sr_image_text_pair_json_in_part-671b3d068f96-000000.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000

# language="ru"
# save_path="xyz_data/${language}/${language}_caption_90k.jsonl"
# python xyz_utils/format_caption.py \
#     --prompt_path xyz_utils/prompt_for_caption.json \
#     --language ${language} \
#     --caption_json xyz_data/${language}/trans_${language}.json \
#     --image_jsonl xyz_data/ru/image_release_v2_ru_image_pure_json_in_part-671a1421951b-000000.jsonl \
#     --image_save_path ${image_save_path} \
#     --save_path  ${save_path}\
#     --data_length 90000

# save_path="xyz_data/${language}/${language}_pair_90k.jsonl"
# jsonl_name="image_release_v2_ru_image_text_pair_json_in_part-671a1c6fbf74-000000.jsonl"
# python xyz_utils/format.py \
#     --image_jsonl xyz_data/${language}/${jsonl_name} \
#     --language ${language} \
#     --prompt_path xyz_utils/prompt.json \
#     --save_path ${save_path} \
#     --image_save_path ${image_save_path} \
#     --data_length 90000