import subprocess
import zipfile
import os


def unzip_file(zip_file_name, mode='rb'):
    '''

    :param zip_file_name:
    :param mode: -Optional parameter, the mode of the zipped file reader
    :return:  返回一个L1C.zip 文件解压后的文件名
    '''

    # 打开zip文件
    zip_file = open(zip_file_name, mode)

    # 利用zipfile解压文件
    zip_fn = zipfile.ZipFile(zip_file)

    # 获取zip文件的所有子目录名和文件名
    namelist = zip_fn.namelist()
    for item in namelist:
        # 提取.zip文件夹的子目录及文件，解压在当前文件夹（‘。’表示当前文件夹
        zip_fn.extract(item, '.')

    # 关闭.zip文件夹
    zip_fn.close()
    zip_file.close()

    print("Unzipping finished!")

    # 返回解压后的文件夹名（）
    return namelist[0]


# 读取Sen2cor.bat文件所在路径
sen2cor_path = r'G:\QiuWanLin\Sen2Cor-02.09.00-win64\Sen2Cor-02.09.00-win64\L2A_Process.bat'

origin_dir = r"G:\QiuWanLin\遥感数据\sentinel\2020"
pattern = '.zip'
output_dir = r"G:\QiuWanLin\遥感数据\sentinel\2020\output"

try:
    os.makedirs(output_dir)

except:
    print('文件夹已存在')

for in_file in os.listdir(origin_dir):

    if pattern in in_file:
        zip_file_path = os.path.join(origin_dir, in_file)
        safe_in_file_path = unzip_file(zip_file_path)
        cmd_args = [sen2cor_path, safe_in_file_path, '--output_dir', output_dir]

        print(f'{safe_in_file_path} processing begin!')

        subprocess.call(cmd_args)

        print(f"{safe_in_file_path} processing finished!\n")

print('All zipped file finished!')
