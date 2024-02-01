import os
import pandas as pd
import numpy as np

data = pd.read_excel("C:\\Users\\CYH10\\Desktop\\名单.xlsx")
column_name = "名单"  # 请替换为你要读取的列的名称
data_set = data[column_name].tolist()
print(data_set)

folder_names = data_set
path = "C:\\Users\\CYH10\\Desktop\\中德国际论坛\\照片"
for name in folder_names:
    folder_path = os.path.join(path, name)
    if not os.path.exists(folder_path):
        try:
            # 创建文件夹
            os.makedirs(folder_path)
            print(f"文件夹 '{name}' 已成功创建于 '{path}'")
        except OSError as e:
            print(f"创建文件夹时发生错误: {e}")
    else:
        print(f"文件夹 '{name}' 已经存在于 '{path}'")
