import pandas as pd
import re


def remove_non_chinese(text):
    return re.sub(r'[\u4e00-\u9fa5]', '', text)


data = pd.read_excel(r"C:\Users\CYH10\Desktop\数据文件\2020农户家庭（原始数据）\2.农户家庭生产情况\D 种植业1表.xlsx")

for column in data.columns:
    if "标题列" in column:
        data.drop(column, axis=1, inplace=True)
        print("true")

for i in enumerate(['HD1_1_n1 ', 'HD1_1_n2', 'HD1_1_n3', 'HD1_1_n4', 'HD1_1_n5', 'HD1_1_n6', 'HD1_1_n7', 'HD1_1_n8', 'HD1_1_n9', 'HD1_1_n10']):
    index, name = i
    rows_to_remove = range(2, len(data[name]+1))
    data.iloc[rows_to_remove][name] = data.iloc[rows_to_remove][name].str.replace('[\u4e00-\u9fa5]+', '')
    # data[name] = data[name][2:3].apply(remove_non_chinese)
# data.to_excel(r"C:\Users\CYH10\Desktop\数据文件\2020农户家庭（原始数据）\2.农户家庭生产情况\D 种植业1表.xlsx", index=False)
