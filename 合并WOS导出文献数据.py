import os

def merge_and_modify_txt_files(folder_path, output_file):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return
    
    # 获取文件夹中所有txt文件的列表
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # 如果没有找到任何txt文件，则打印错误信息并返回
    if not txt_files:
        print(f"Error: No txt files found in the folder '{folder_path}'.")
        return

    # 打开输出文件，准备写入头部信息
    with open(output_file, 'w') as output:

        # 遍历每个txt文件并合并、修改内容
        for txt_file in txt_files:
            i = 1
            file_path = os.path.join(folder_path, txt_file)

            # 打开txt文件，读取内容
            with open(file_path, 'r') as input_file:
                # 仅保存一次前两行
                if i == 1:
                    lines = input_file.readlines()[0:]
                    i = i+1
                else:
                    lines = input_file.readlines()[2:]

                # 将剩余的内容写入输出文件
                output.writelines(lines)

    print(f"Files merged and modified successfully. Output saved to '{output_file}'.")

# 指定文件夹路径和输出文件路径
folder_path = "your_folder_path"  # 替换为你的文件夹路径
output_file = "output.txt"  # 替换为你的输出文件路径

# 调用函数
merge_and_modify_txt_files(folder_path, output_file)
