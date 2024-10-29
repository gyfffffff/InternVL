import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='move safe images')
    parser.add_argument('--language', type=str, required=True, help='language')
    parser.add_argument('--image_type', type=str, required=True, help='image_type')
    parser.add_argument('--jsonl_name', type=str, required=True, help='jsonl_name')
    parser.add_argument('--save_path', type=str, required=True, help='save_path')
    args = parser.parse_args()
    download(args)