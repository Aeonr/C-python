import pandas as pd

data = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx', header=1)
print(data)
# D:\Kugou\咸阳站逐日平均流量表.xlsx，是需要修改数据格式的文件路径，存放文件的地址，绝对路径
lieshu = data.shape[1]  # 取dataframe列的数量
l1 = data.iloc[:31, [0, 1]]  # 选择第1,2列数值
print(l1)
lie = data.columns.values[1]  # 按位置提取列标题
print(lie)
month = []  # 定义month列表增加一列月份
for i in l1['时间']:
    month.append(lie)  # 用月份列列名填充1列数据
l1 = l1.copy()
l1.rename(columns={lie: '日径流'}, inplace=True)  # 改径流列名统一为‘日径流’，便于合并时同列
l1['月'] = month  # 增加一列并用month列表赋值
for ii in range(2, 13):  # 从第3列开始选择1,3列，1,4列.....
    lietemp = data.iloc[:31, [0, ii]]
    lie = data.columns.values[ii]  # 按位置提取列标题
    month = []
    for i in lietemp['时间']:
        month.append(lie)
    lietemp = lietemp.copy()
    lietemp.rename(columns={lie: '日径流'}, inplace=True)
    lietemp['月'] = month
    l1 = pd.concat([l1, lietemp])
print(l1)
# l1=l1.sort_index()
# print(l1)
l1.to_excel('"E:\\建模比赛\\咸阳日径流1979-2019 output.xlsx"', index=False)
# D:\Kugou\shiyan1.xlsx，是保存文件的路径地址，可以根据自己保存路径修改一下
