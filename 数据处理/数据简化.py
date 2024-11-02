import pandas as pd
import numpy as np

data = pd.read_excel(r"C:\Users\CYH10\Desktop\gmnl实例\data.xlsx", header=0)
# print(data['id'])

# 随即简化
# np.random.seed(42)
#
# sample_data = data.sample(n=2000, replace=True)
#
# sample_data.to_stata(r"C:\Users\CYH10\Desktop\gmnl实例\data_simple.xlsx")
data['ID'] = data['ID'].astype(int)
# 删除简化
data.drop(data[data['ID'] > 200].index, inplace=True)

data.to_excel(r"C:\Users\CYH10\Desktop\gmnl实例\data_simple.xlsx", index=False)
