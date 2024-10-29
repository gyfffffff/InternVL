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
    file_key = f'image/release_v2/{language}/{image_type}/json_in/{jsonl_name}'
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')

    # 将文件内容解析为JSON对象
    json_objects = [json.loads(line) for line in StringIO(file_content)]
    error_indices = []
    i=0
    # 输出JSON对象
    for obj in tqdm(json_objects):
        try:
            img_id = obj.get('img_id')
            # print(img_id)
            outer_dict = obj.get('image', {})
            inner_value = outer_dict.get('path')
            # print(inner_value)
            
            bucket_name = 'xyz-process-2'
            key = f"image/release_v2/{language}/{image_type}/img/{img_id}"

            # 下载图片到本地文件
            local_file_dir = f"{save_path}/{language}/{image_type}/"
            local_file_path = local_file_dir + img_id
            os.makedirs(os.path.dirname(local_file_dir), exist_ok=True)
            s3.download_file(bucket_name, key, local_file_path)
            # print(f"Image downloaded to {local_file_path}")
            i+=1
        except Exception as e:
        # 如果发生ValueError，将i的值添加到列表中
            error_indices.append(img_id)
            print(e)

    print("Indices that caused errors:", error_indices)
    print("保存图片张数：",i)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--language", type=str, default="")
    args.add_argument("--image_type", type=str, default="")
    args.add_argument("--jsonl_name", type=str, default="")
    args.add_argument("--save_path", type=str, default="")
    args = args.parse_args()
    download(args)
