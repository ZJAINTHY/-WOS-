import os

def merge_and_modify_txt_files(folder_path, output_file):
    # ����ļ����Ƿ����
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return
    
    # ��ȡ�ļ���������txt�ļ����б�
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # ���û���ҵ��κ�txt�ļ������ӡ������Ϣ������
    if not txt_files:
        print(f"Error: No txt files found in the folder '{folder_path}'.")
        return

    # ������ļ���׼��д��ͷ����Ϣ
    with open(output_file, 'w') as output:

        # ����ÿ��txt�ļ����ϲ����޸�����
        for txt_file in txt_files:
            i = 1
            file_path = os.path.join(folder_path, txt_file)

            # ��txt�ļ�����ȡ����
            with open(file_path, 'r') as input_file:
                # ������һ��ǰ����
                if i == 1:
                    lines = input_file.readlines()[0:]
                    i = i+1
                else:
                    lines = input_file.readlines()[2:]

                # ��ʣ�������д������ļ�
                output.writelines(lines)

    print(f"Files merged and modified successfully. Output saved to '{output_file}'.")

# ָ���ļ���·��������ļ�·��
folder_path = "your_folder_path"  # �滻Ϊ����ļ���·��
output_file = "output.txt"  # �滻Ϊ�������ļ�·��

# ���ú���
merge_and_modify_txt_files(folder_path, output_file)
