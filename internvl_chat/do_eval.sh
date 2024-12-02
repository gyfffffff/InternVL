AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language AR --dynamic
AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_80k slvqa_caption --language AR --dynamic

AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language HU --dynamic
AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_caption_90k slvqa_caption --language HU --dynamic


