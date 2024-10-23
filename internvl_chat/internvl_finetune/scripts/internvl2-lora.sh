#!/bin/bash

#加载环境信息
module load anaconda/2022.10
module load cuda/11.8
source activate internvl

nvidia-smi
#刷新日志缓存
export PYTHONUNBUFFERED=1


# ar image-text-pair
GPUS=8 PER_DEVICE_BATCH_SIZE=1 sh shell/internvl2.0/2nd_finetune/internvl2_1b_qwen2_0_5b_dynamic_res_2nd_finetune_lora.sh

