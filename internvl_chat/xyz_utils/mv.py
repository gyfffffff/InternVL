import shutil
import os

def move_files(src_dir, dest_dir):

    # 遍历源目录中的所有文件
    for filename in os.listdir(src_dir):
        # 构建完整的文件路径
        src_file = os.path.join(src_dir, filename)
        # 确保是文件而不是目录
        if os.path.isfile(src_file):
            # 移动文件
            shutil.move(src_file, dest_dir)
            print(f"文件 {filename} 已移动到 {dest_dir}。")

# 设置源目录和目标目录
source_directory = '/mnt/workspace/gaoyufei/xyz_v2_data/th'  # 替换为你的源目录路径
destination_directory = '/mnt/workspace/gaoyufei/xyz_v2_data/th/image_text_pair'  # 替换为你的目标目录路径

# 调用函数移动文件
move_files(source_directory, destination_directory)
