from meteostat import Stations, Point, Daily
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pandas as pd
import os

ll_data = pd.read_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\市映射表.xlsx")
data_export = pd.DataFrame()
# 定义气象站
stations = Stations()
stations = stations.region('CN')  # 'CN' 是中国的 ISO 3166 国家代码

for i in range(len(ll_data)):
    print(ll_data.iloc[i]['省份城市'])
    stations = stations.nearby(ll_data.iloc[i]['纬度'], ll_data.iloc[i]['经度'])  # 定义坐标
    station_list = stations.fetch(10)
    station_id = station_list.index[0]
    data = Daily(station_id, start=datetime(2000, 1, 1), end=datetime(2022, 12, 31))
    data = data.fetch()

    data.insert(0, '市', ll_data.iloc[i]['省份城市'])
    data_export = data_export._append(data)

data_export.to_excel('Daily.xlsx')
# data.to_csv('Daily.csv')

