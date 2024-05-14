from xpinyin import Pinyin
import pandas as pd
import numpy as np

data = pd.read_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\地市列表.xlsx")
data['拼音'] = np.zeros(len(data), dtype=str)
p = Pinyin()
for i in range(len(data)):
    if data['地级市'][i][-1] == '市':
        data.loc[i, "拼音"] = p.get_pinyin(data['地级市'][i][:-1], '')
    else:
        data.drop(i, inplace=True)

data.to_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\地市列表_拼音.xlsx", index=False)
