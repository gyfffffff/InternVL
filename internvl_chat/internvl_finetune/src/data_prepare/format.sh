# ar pair 1/4
# python src/data/format.py \
#     --data_root_path /data/xyz \
#     --save_root /data/xyz/InternVL-finetune/data \
#     --raw_jsonl_path /data/xyz/InternVL-finetune/data/ar/image_text_pair/raw/v001_part-666c3ce73bf5-000000.jsonl \
#     --lang ar \
#     --image_type image_pure \
#     --prompt_path /data/xyz/InternVL-finetune/prompt/prompt_image-text-pair.json


# ar pure 4/4
python src/data/format.py \
    --data_root_path /data/xyz \
    --save_root /data/xyz/InternVL-finetune/data \
    --raw_jsonl_path /data/xyz/InternVL-finetune/data/ar/image_pure/raw/v004_part-66752f1b9270-000000.jsonl \
    --lang ar \
    --image_type image_pure \
    --prompt_path /data/xyz/InternVL-finetune/prompt/prompt_image-pure.json