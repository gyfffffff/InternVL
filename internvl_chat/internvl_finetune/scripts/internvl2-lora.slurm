#!/bin/bash


name=internvl2-lora
sbatch -N 1 \
    -n 10 \
    --gres=gpu:8 \
    -p adg_2 \
    -A adg_2 \
    -o /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/scripts/${name}.out \
    -e /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/scripts/${name}.err \
    /ailab/user/gaoyufei/InternVL/internvl_chat/internvl_finetune/scripts/internvl2-lora.sh \




