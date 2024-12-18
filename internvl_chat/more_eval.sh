# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_80k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_cs_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ko_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ru_caption_40k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_sr_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_th_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_caption_90k mme --dynamic
# GPUS=1 bash evaluate.sh pretrained/InternVL2-8B mme --dynamic


GPUS=2 bash evaluate.sh pretrained/InternVL2-8B mmbench-dev-en --dynamic
GPUS=2 bash evaluate.sh pretrained/InternVL2-8B mmbench-test-en --dynamic
GPUS=2 bash evaluate.sh pretrained/InternVL2-8B mmbench-dev-cn --dynamic
GPUS=2 bash evaluate.sh pretrained/InternVL2-8B mmbench-test-cn --dynamic