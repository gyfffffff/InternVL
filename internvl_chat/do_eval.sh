# GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_1b_qwen2_0_5b_dynamic_res_2nd_finetune_lora \
#     vqa-textvqa-val --dynamic

# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh pretrained/InternVL2-8B slvqa --dynamic
AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_oldprompt_ar_100k slvqa --dynamic