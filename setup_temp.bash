module load anaconda/2022.10
module load cuda/11.8
source activate internvl

pip install -r requirements.txt

huggingface-cli download --resume-download --local-dir-use-symlinks False OpenGVLab/InternVL2-1B --local-dir /ailab/user/gaoyufei/InternVL/internvl_chat/pretrained/InternVL2-1B


