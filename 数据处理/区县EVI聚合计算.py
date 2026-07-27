import os
import pandas as pd
import numpy as np


data_dir = "/Users/aeon/Desktop/GEE_China_County_EVI"

invalid_val = -9999

# 读取目录下所有csv文件
file_list = [f for f in os.listdir(data_dir) if f.lower().endswith(".csv")]
file_list.sort()

monthly_list = []
for filename in file_list:
    file_path = os.path.join(data_dir, filename)
    df = pd.read_csv(file_path, encoding='gbk')
    
    # 无效值替换为NaN，均值计算自动忽略NaN
    df["EVI"] = df["EVI"].replace(invalid_val, np.nan)
    # 保留核心字段
    monthly_list.append(df[["county_code", "county", "province", "year", "month", "EVI"]])

# 合并全部月度数据
df_all = pd.concat(monthly_list, axis=0, ignore_index=True)

# ========== 方式1：长格式结果（推荐，一行=区县+单一年份年均EVI） ==========
df_year_long = df_all.groupby(
    ["county_code", "county", "province", "year"]
)["EVI"].mean().reset_index()

# 保存长表
df_year_long.to_csv("/Users/aeon/Desktop/EVI_区县年均值.csv", index=False)