from meteostat import Stations, Point, Daily
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pandas as pd
import os

# 尝试删除文件，如果文件不存在则捕获 FileNotFoundError 错误
try:
    os.remove('Daily.csv')
except FileNotFoundError:
    print(f"文件 {'Daily.csv'} 不存在，无法删除。")


# 查找北京附近的气象站
stations = Stations()
stations = stations.region('CN')  # 'CN' 是中国的 ISO 3166 国家代码
# stations = stations.nearby(39.9042, 116.4074)  # 北京市的坐标
station_list = stations.fetch()
station_list.to_excel('station.xlsx')
data = pd.DataFrame()
# 打印找到的前10个气象站信息
print(station_list)
for i in range(len(station_list)):
    # 选择第一个气象站的 ID
    station_id = station_list.index[i]
    # 下载该气象站的每日数据
    new_data = Daily(station_list, start=datetime(2000, 1, 1), end=datetime(2024, 1, 1))
    data = data.append(new_data.fetch(), ignore_index=True)
    print(f"已下载 {i+1} 个气象站的数据")
data.to_csv('Daily.csv')

