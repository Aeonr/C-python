# coding:utf-8
from matplotlib import pyplot as plt
from tqdm import tqdm
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind




# 传入时间序列以及待检验数据
# data:数据， step：步长， sig_level：显著水平
def huaTTest(data, step, sig_level):
    datacount = len(data)
    v = 2*step-2  # 自由度
    t_value = 2.31  # t检验值
    n1 = step
    n2 = step
    t = np.zeros(len(data))
    c = 1.0 / n1 + 1.0 / n2

    for i in range(step-1, datacount-step):
        data1 = data[i-step+1:i+1]
        data2 = data[i+1:i+step+1]
        # 计算均值
        x1_mean = data1.mean()
        x2_mean = data2.mean()
        # 计算方差
        s1 = data1.var()
        s2 = data2.var()
        sw2 = (n1*s1 + n2*s2)/(n1+n2-2.0)
        t[i - step + 1] = (x1_mean - x2_mean) / np.sqrt(sw2 * c)
    return t, t_value

plt.rcParams['font.family'] = ['SimHei']  # 设置字体
plt.rcParams['axes.unicode_minus'] = False

# 获取数据
d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx', sheet_name='Sheet3')

# 获取时间列以及casa模拟值
time = np.array(d['年'])
casa = np.array(d['咸阳年径流'])
datacount = len(casa)

step=5
t, t_value = huaTTest(casa, step, 0.05)

t = t[t != 0]

sig_values = []  # 存储显著变化值
for i in range(len(t)):
    if np.abs(t[i]) > t_value:
        sig_values.append(time[i + step - 1])



fig, ax = plt.subplots(figsize=(9, 5), sharey=True)

fontdict = {'size': 12, 'color': 'k'}

x = time[step-1:datacount-step]
ax.set_xticks(x[::2])
# ax.set_xlim((time[0], time[datacount-step]))
ax.plot(x, t, c='k', linewidth=1.5, label=u'滑动T值', zorder=1)
# 添加显著水平线
ax.hlines(y=t_value, xmin=np.min(x), xmax=np.max(x), linewidth=1.5, linestyles='--', label=u'0.05显著水平')
ax.hlines(y=-t_value, xmin=np.min(x), xmax=np.max(x), linewidth=1.5, linestyles='--', label=None)
# 修改刻度线指向
ax.tick_params(left=True, bottom=True, direction='in', labelsize=12)
# 添加坐标轴标签
ax.set_xlabel(u'年份 Year', fontdict=fontdict)
ax.set_ylabel('T', fontdict=fontdict)
# 设置图例
ax.legend(bbox_to_anchor=(0.95, 0.95), facecolor='w', frameon=False)
plt.show()



huaTTest(casa, 5, 0.05)
print(sig_values)
