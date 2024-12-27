import pandas as pd
from scipy.stats import ttest_ind, levene, normaltest, ttest_rel, f_oneway, kruskal
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

diopter = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='屈光度')
axial = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='眼轴长')
choroid = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='脉络膜厚度')

diopter_feeder_base = diopter.loc[diopter['组别'] == '哺光仪组', '基线数据'].agg(list)
diopter_feeder_1 = diopter.loc[diopter['组别'] == '哺光仪组', '第一次复查'].agg(list)
diopter_feeder_1 = [x - (-3.51) for x in diopter_feeder_1]
diopter_feeder_2 = diopter.loc[diopter['组别'] == '哺光仪组', '第二次复查'].agg(list)
diopter_feeder_2 = [x - (-3.51) for x in diopter_feeder_2]
diopter_feeder_3 = diopter.loc[diopter['组别'] == '哺光仪组', '第三次复查'].agg(list)
diopter_feeder_3 = [x - (-3.51) for x in diopter_feeder_3]
diopter_feeder_4 = diopter.loc[diopter['组别'] == '哺光仪组', '第四次复查'].agg(list)
diopter_feeder_4 = [x - (-3.51) for x in diopter_feeder_4]

diopter_cnc_base = diopter.loc[diopter['组别'] == 'CNC组', '基线数据'].agg(list)
diopter_cnc_1 = diopter.loc[diopter['组别'] == 'CNC组', '第一次复查'].agg(list)
diopter_cnc_1 = [x - (-1.75) for x in diopter_cnc_1]
diopter_cnc_2 = diopter.loc[diopter['组别'] == 'CNC组', '第二次复查'].agg(list)
diopter_cnc_2 = [x - (-1.75) for x in diopter_cnc_2]
diopter_cnc_3 = diopter.loc[diopter['组别'] == 'CNC组', '第三次复查'].agg(list)
diopter_cnc_3 = [x - (-1.75) for x in diopter_cnc_3]
diopter_cnc_4 = diopter.loc[diopter['组别'] == 'CNC组', '第四次复查'].agg(list)
diopter_cnc_4 = [x - (-1.75) for x in diopter_cnc_4]

diopter_con_base = diopter.loc[diopter['组别'] == '对照组', '基线数据'].agg(list)
diopter_con_1 = diopter.loc[diopter['组别'] == '对照组', '第一次复查'].agg(list)
diopter_con_1 = [x - (-2.03) for x in diopter_con_1]
diopter_con_2 = diopter.loc[diopter['组别'] == '对照组', '第二次复查'].agg(list)
diopter_con_2 = [x - (-2.03) for x in diopter_con_2]
diopter_con_3 = diopter.loc[diopter['组别'] == '对照组', '第三次复查'].agg(list)
diopter_con_3 = [x - (-2.03) for x in diopter_con_3]
diopter_con_4 = diopter.loc[diopter['组别'] == '对照组', '第四次复查'].agg(list)
diopter_con_4 = [x - (-2.03) for x in diopter_con_4]

axial_feeder_base = axial.loc[axial['组别'] == '哺光仪组', '基线数据'].agg(list)
axial_feeder_1 = axial.loc[axial['组别'] == '哺光仪组', '第一次复查'].agg(list)
axial_feeder_1 = [x - 24.85 for x in axial_feeder_1]
axial_feeder_2 = axial.loc[axial['组别'] == '哺光仪组', '第二次复查'].agg(list)
axial_feeder_2 = [x - 24.85 for x in axial_feeder_2]
axial_feeder_3 = axial.loc[axial['组别'] == '哺光仪组', '第三次复查'].agg(list)
axial_feeder_3 = [x - 24.85 for x in axial_feeder_3]
axial_feeder_4 = axial.loc[axial['组别'] == '哺光仪组', '第四次复查'].agg(list)
axial_feeder_4 = [x - 24.85 for x in axial_feeder_4]

axial_cnc_base = axial.loc[axial['组别'] == 'CNC组', '基线数据'].agg(list)
axial_cnc_1 = axial.loc[axial['组别'] == 'CNC组', '第一次复查'].agg(list)
axial_cnc_1 = [x - 23.81 for x in axial_cnc_1]
axial_cnc_2 = axial.loc[axial['组别'] == 'CNC组', '第二次复查'].agg(list)
axial_cnc_2 = [x - 23.81 for x in axial_cnc_2]
axial_cnc_3 = axial.loc[axial['组别'] == 'CNC组', '第三次复查'].agg(list)
axial_cnc_3 = [x - 23.81 for x in axial_cnc_3]
axial_cnc_4 = axial.loc[axial['组别'] == 'CNC组', '第四次复查'].agg(list)
axial_cnc_4 = [x - 23.81 for x in axial_cnc_4]

axial_con_base = axial.loc[axial['组别'] == '对照组', '基线数据'].agg(list)
axial_con_1 = axial.loc[axial['组别'] == '对照组', '第一次复查'].agg(list)
axial_con_1 = [x - 24.31 for x in axial_con_1]
axial_con_2 = axial.loc[axial['组别'] == '对照组', '第二次复查'].agg(list)
axial_con_2 = [x - 24.31 for x in axial_con_2]
axial_con_3 = axial.loc[axial['组别'] == '对照组', '第三次复查'].agg(list)
axial_con_3 = [x - 24.31 for x in axial_con_3]
axial_con_4 = axial.loc[axial['组别'] == '对照组', '第四次复查'].agg(list)
axial_con_4 = [x - 24.31 for x in axial_con_4]

choroid_feeder_base = choroid.loc[choroid['组别'] == '哺光仪组', '基线数据'].agg(list)
choroid_feeder_1 = choroid.loc[choroid['组别'] == '哺光仪组', '第一次复查'].agg(list)
choroid_feeder_1 = [x - 268.35 for x in choroid_feeder_1]
choroid_feeder_2 = choroid.loc[choroid['组别'] == '哺光仪组', '第二次复查'].agg(list)
choroid_feeder_2 = [x - 268.35 for x in choroid_feeder_2]
choroid_feeder_3 = choroid.loc[choroid['组别'] == '哺光仪组', '第三次复查'].agg(list)
choroid_feeder_3 = [x - 268.35 for x in choroid_feeder_3]
choroid_feeder_4 = choroid.loc[choroid['组别'] == '哺光仪组', '第四次复查'].agg(list)
choroid_feeder_4 = [x - 268.35 for x in choroid_feeder_4]

choroid_cnc_base = choroid.loc[choroid['组别'] == 'CNC组', '基线数据'].agg(list)
choroid_cnc_1 = choroid.loc[choroid['组别'] == 'CNC组', '第一次复查'].agg(list)
choroid_cnc_1 = [x - 302.5 for x in choroid_cnc_1]
choroid_cnc_2 = choroid.loc[choroid['组别'] == 'CNC组', '第二次复查'].agg(list)
choroid_cnc_2 = [x - 302.5 for x in choroid_cnc_2]
choroid_cnc_3 = choroid.loc[choroid['组别'] == 'CNC组', '第三次复查'].agg(list)
choroid_cnc_3 = [x - 302.5 for x in choroid_cnc_3]
choroid_cnc_4 = choroid.loc[choroid['组别'] == 'CNC组', '第四次复查'].agg(list)
choroid_cnc_4 = [x - 302.5 for x in choroid_cnc_4]

choroid_con_base = choroid.loc[choroid['组别'] == '对照组', '基线数据'].agg(list)
choroid_con_1 = choroid.loc[choroid['组别'] == '对照组', '第一次复查'].agg(list)
choroid_con_1 = [x - 314.05 for x in choroid_con_1]
choroid_con_2 = choroid.loc[choroid['组别'] == '对照组', '第二次复查'].agg(list)
choroid_con_2 = [x - 314.05 for x in choroid_con_2]
choroid_con_3 = choroid.loc[choroid['组别'] == '对照组', '第三次复查'].agg(list)
choroid_con_3 = [x - 314.05 for x in choroid_con_3]
choroid_con_4 = choroid.loc[choroid['组别'] == '对照组', '第四次复查'].agg(list)
choroid_con_4 = [x - 314.05 for x in choroid_con_4]

# 横坐标
plt.figure(1, figsize=(5, 4))
x1 = ["第一次复查", "第二次复查", "第三次复查", "第四次复查"]

# 各组数据
y1 = [np.mean(diopter_feeder_1), np.mean(diopter_feeder_2), np.mean(diopter_feeder_3), np.mean(diopter_feeder_4)]  # 哺光仪组数据，示例数据
y2 = [np.mean(diopter_cnc_1), np.mean(diopter_cnc_2), np.mean(diopter_cnc_2), np.mean(diopter_cnc_2)]   # CNC组数据，示例数据
y3 = [np.mean(diopter_con_1), np.mean(diopter_con_2), np.mean(diopter_con_3), np.mean(diopter_con_4)]   # 对照组数据，示例数据

# 创建折线图
plt.plot(x1, y1, label='哺光仪组', color='blue', linestyle='-', marker='o')
plt.plot(x1, y2, label='CNC组', color='green', linestyle='--', marker='s')
plt.plot(x1, y3, label='对照组', color='red', linestyle='-.', marker='^')

# 添加标题和标签
plt.title("复查结果折线图")
plt.xlabel("时间")
plt.ylabel("屈光度")
# 添加图例
plt.legend()

plt.figure(2, figsize=(5, 4))
x2 = ["第一次复查", "第二次复查", "第三次复查", "第四次复查"]

# 各组数据
y4 = [np.mean(choroid_feeder_1), np.mean(choroid_feeder_2), np.mean(choroid_feeder_3), np.mean(choroid_feeder_4)]  # 哺光仪组数据，示例数据
y5 = [np.mean(choroid_cnc_1), np.mean(choroid_cnc_2), np.mean(choroid_cnc_2), np.mean(choroid_cnc_2)]   # CNC组数据，示例数据
y6 = [np.mean(choroid_con_1), np.mean(choroid_con_2), np.mean(choroid_con_3), np.mean(choroid_con_4)]   # 对照组数据，示例数据

# 创建折线图
plt.plot(x2, y4, label='哺光仪组', color='blue', linestyle='-', marker='o')
plt.plot(x2, y5, label='CNC组', color='green', linestyle='--', marker='s')
plt.plot(x2, y6, label='对照组', color='red', linestyle='-.', marker='^')

# 添加标题和标签
plt.title("复查结果折线图")
plt.xlabel("时间")
plt.ylabel("眼轴长")
# 添加图例
plt.legend()

plt.figure(3, figsize=(5, 4))
x3 = ["第一次复查", "第二次复查", "第三次复查", "第四次复查"]

# 各组数据
y7 = [np.mean(axial_feeder_1), np.mean(axial_feeder_2), np.mean(axial_feeder_3), np.mean(axial_feeder_4)]  # 哺光仪组数据，示例数据
y8 = [np.mean(axial_cnc_1), np.mean(axial_cnc_2), np.mean(axial_cnc_2), np.mean(axial_cnc_2)]   # CNC组数据，示例数据
y9 = [np.mean(axial_con_1), np.mean(axial_con_2), np.mean(axial_con_3), np.mean(axial_con_4)]   # 对照组数据，示例数据

# 创建折线图
plt.plot(x2, y7, label='哺光仪组', color='blue', linestyle='-', marker='o')
plt.plot(x2, y8, label='CNC组', color='green', linestyle='--', marker='s')
plt.plot(x2, y9, label='对照组', color='red', linestyle='-.', marker='^')

# 添加标题和标签
plt.title("复查结果折线图")
plt.xlabel("时间")
plt.ylabel("脉络膜厚度")
# 添加图例
plt.legend()

plt.show()