# ar pair 1/4
python src/data_prepare/format.py \
    --workdir_root /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune \
    --raw_jsonl_path /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/data/ar/image_text_pair/v001_part-666c3ce73bf5-000000.jsonl \
    --language ar \
    --image_type image_text_pair \
    --prompt_path /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/prompt/prompt_image-text-pair.json \
    --save_root /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/data \
    --image_save_file /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/data/ar/image_text_pair_save.txt \


# # ar pure 4/4
# python src/data/format.py \
#     --data_root_path /data/xyz \
#     --save_root /data/xyz/InternVL-finetune/data \
#     --raw_jsonl_path /data/xyz/InternVL-finetune/data/ar/image_pure/raw/v004_part-66752f1b9270-000000.jsonl \
#     --lang ar \
#     --image_type image_pure \
#     --prompt_path /data/xyz/InternVL-finetune/prompt/prompt_image-pure.json