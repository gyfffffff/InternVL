# bash xyz_utils/format.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_75k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_75k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_50k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_100k.sh
# GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_vi_10k.sh

cd /mnt/workspace/feijiaying/InternVL/examples/ar
# unzip -d /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure image_pure3.zip
# find /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/image_pure3/ -name "*" -exec mv {} /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/ \;
# unzip -o -d /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure image_pure4.zip
# find /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/image_pure4/ -name "*" -exec mv {} /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/ \;

find /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/image_pure2/ -name "*" -exec mv {} /mnt/workspace/gaoyufei/xyz_v2_data/ar/image_pure/ \;



cd /mnt/workspace/gaoyufei/InternVL/internvl_chat
GPUS=2 PER_DEVICE_BATCH_SIZE=2 bash shell/internvl2.0/2nd_finetune/internvl2_8b_internlm2_7b_dynamic_res_2nd_finetune_lora_ar_caption_100k.sh



