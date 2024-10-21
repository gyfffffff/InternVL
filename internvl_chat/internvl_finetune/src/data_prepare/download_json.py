import boto3
import json
from io import StringIO
from tqdm import tqdm
import botocore
import argparse
import os


def download(args):
    language = args.language
    image_type = args.image_type
    jsonl_name = args.jsonl_name
    save_path = args.save_path

    s3 = boto3.client(
                "s3",
                aws_access_key_id = "QFG6687OWYZZUZ3YJ5WS",
                aws_secret_access_key = "ABUxuE6dOiBfAcdiMEH0FGHOjnrcfEdgYfvnuWec",
                endpoint_url = "http://10.140.85.161",
                # config=Config(s3={"addressing_style": "path"}, retries={"max_attempts": 8, "mode": "standard"}),
            )
    print('connect to client successfully!')

    # 指定要下载的S3对象的桶名和键名

    bucket_name = 'xyz-process-2'
    file_key = f'image/release/{language}/{image_type}/json_in/{jsonl_name}'

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')
    os.makedirs(f"{save_path}/{language}/{image_type}/raw", exist_ok=True)
    with open(f"{save_path}/{language}/{image_type}/raw/{jsonl_name}", 'w') as f:
        for line in StringIO(file_content):
            f.write(line)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--language", type=str, default="")
    args.add_argument("--image_type", type=str, default="")
    args.add_argument("--jsonl_name", type=str, default="")
    args.add_argument("--save_path", type=str, default="")
    args = args.parse_args()
    download(args)
