import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def MTT(data, step):
    n = len(data)
    v = step + step - 2  # 自由度
    t = np.zeros((n - step - step + 1))
    ss = np.sqrt(1 / step + 1 / step)

    ttest = 2.31  # step=5,alpha=0.05，这个需要根据需要查表做改动

    for i in range(len(t)):
        n1 = data[i:i + step]
        n2 = data[i + step:i + step + step]
        x1 = np.mean(n1)  # 平均值
        x2 = np.mean(n2)
        s1 = np.std(n1)  # 方差
        s2 = np.std(n2)
        s = np.sqrt((step * s1 * s1 + step * s2 * s2) / v)
        t[i] = (x1 - x2) / (s * ss)
        print(t[i])
        if t[i]>2.31 or t[i]<-2.31:
            print(i)


    plt.plot(t, label = "滑动T值(step=%s)" % step)
    plt.axhline(0, ls="--", c="k")
    plt.axhline(ttest, ls="--", c="r", label='95%显著区间')
    plt.axhline(-ttest, ls="--", c="r")
    plt.legend(loc='upper center', frameon=False, ncol=2, fontsize=14)  # 图例
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()

    return t
d = pd.read_excel('E:\\建模比赛\\林家村日径流深1970-2014.xlsx', sheet_name='年径流量')
data = d['年径流'][0:46]
# d = pd.read_excel('E:\\建模比赛\\林家村月均流量资料.xls',sheet_name='Sheet2')
# data = d['径流量'][0:74]

MTT(data, 5)