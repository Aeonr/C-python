import pandas as pd

# 读取Excel文件
df = pd.read_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\省市区经纬度映射表.xlsx")

data = df.values.tolist()
new_data_shi = pd.DataFrame()
new_data_county = pd.DataFrame()

for i in range(len(data)):
    if data[i][1][-1] == "市":
        new_data_shi = new_data_shi._append(df.iloc[i])
    elif data[i][1][-1] == "区" or data[i][1][-1] == "县":
        new_data_county = new_data_county._append(df.iloc[i])

# 保存为新的Excel文件
new_data_shi = new_data_shi.drop_duplicates(keep='first')
new_data_county = new_data_county.drop_duplicates(keep='first')
new_data_shi.to_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\市映射表.xlsx", index=False)
new_data_county.to_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\区县映射表.xlsx", index=False)
