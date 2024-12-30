# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language AR --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language HU --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language VI --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language KO --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language TH --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language SR --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language CS --dynamic
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 MASTER_PORT=63668 bash evaluate.sh pretrained/InternVL2-8B slvqa_caption --language RU --dynamic


# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_gptcaption_75k gpt4o_caption --language AR --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_gptcaption_75k gpt4o_caption --language HU --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_caption_90k slvqa_caption --language VI --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_th_caption_90k slvqa_caption --language TH --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_sr_caption_90k slvqa_caption --language SR --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ru_caption_40k slvqa_caption --language RU --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_cs_caption_90k slvqa_caption --language CS --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ko_caption_90k slvqa_caption --language KO --dynamic --temperature 0.5



# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language th --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_th_caption_90k --results_file xyz_caption_results/gpt4o_caption_th_241225033752.json 
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language ko --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ko_caption_90k --results_file xyz_caption_results/gpt4o_caption_ko_241225124322.json 
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language ru --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ru_caption_40k --results_file xyz_caption_results/gpt4o_caption_ru_241225085335.json 
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language sr --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_sr_caption_90k --results_file xyz_caption_results/gpt4o_caption_sr_241225061112.json 
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language cs --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_cs_caption_90k --results_file xyz_caption_results/gpt4o_caption_cs_241225105827.json 
AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language hu --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_gptcaption_75k --results_file xyz_caption_results/gpt4o_caption_hu_241227114641.json 
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language ar --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_90k --results_file xyz_caption_results/gpt4o_caption_ar_241224202540.json
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java python eval/slvqa_caption/calculation.py --language vi --checkpoint work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_caption_90k --results_file xyz_caption_results/gpt4o_caption_vi_241225010426.json 



# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_80k gpt4o_caption --language AR --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_hu_caption_90k gpt4o_caption --language HU --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_caption_90k gpt4o_caption --language VI --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_th_caption_90k gpt4o_caption --language TH --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_sr_caption_90k gpt4o_caption --language SR --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ru_caption_40k gpt4o_caption --language RU --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_cs_caption_90k gpt4o_caption --language CS --dynamic --temperature 0.5
# AAC_METRICS_JAVA_PATH=/mnt/workspace/gaoyufei/jdk1.8.0/bin/java GPUS=2 bash evaluate.sh work_dirs/internvl_chat_v2_0/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ko_caption_90k gpt4o_caption --language KO --dynamic --temperature 0.5





