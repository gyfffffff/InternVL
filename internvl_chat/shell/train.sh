# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_sr_caption_90k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_caption_90k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_cs_caption_90k.sh
GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_caption_90k.sh
GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_th_caption_90k.sh
GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ko_caption_90k.sh
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_80k slvqa --dynamic