# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
#
# def Pettitt(data):
#     data = np.array(data)
#     n = len(data)
#     sk = [0]
#
#     for i in range(1, n):
#         s = 0
#         for j in range(i):
#             if data[i] > data[j]:
#                 s = s + 1
#             if data[i] < data[j]:
#                 s = s - 1
#             else:
#                 s = s + 0
#         sk.append(s)
#
#     k = np.max(sk)
#     kt = sk.index(max(sk))
#     print(k, kt)
#     p = 2 * np.exp((-6 * (k ** 2)) / (n ** 3 + n ** 2))
#
#     if p <= 0.05:
#         a = '显著'
#     else:
#         a = '不显著'
#     print('突变点位置:%s, %s' % (kt, a))
#
#     # 画图
#     plt.plot(range(len(data)), data)
#     plt.plot([0, kt], [np.mean(data[0:kt]), np.mean(data[0:kt])], color='r', linestyle='--')
#     plt.plot([kt, len(data)], [np.mean(data[kt::]), np.mean(data[kt::])], color='r', linestyle='--')
#     plt.axvline(x=kt, ls="--", c="g")
#     plt.xticks(fontsize=16)
#     plt.yticks(fontsize=16)
#     plt.rcParams['font.sans-serif'] = ['KaiTi']
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.show()
#
#     return k, kt  # ,Pettitt_result
#
# #d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx')
# #data = d['咸阳年径流'][0:41]
# d = pd.read_excel('E:\\建模比赛\\林家村日径流深1970-2014.xlsx', sheet_name='年径流量')
# data = d['年径流'][9:]
# Pettitt(data)

import pandas as pd
import numpy as np


def Pettitt_change_point_detection(inputdata):
    inputdata = np.array(inputdata)
    n = inputdata.shape[0]
    k = range(n)
    inputdataT = pd.Series(inputdata)
    r = inputdataT.rank()
    Uk = [2*np.sum(r[0:x])-x*(n + 1) for x in k]
    Uka = list(np.abs(Uk))
    U = np.max(Uka)
    K = Uka.index(U)
    pvalue = 2 * np.exp((-6 * (U**2))/(n**3 + n**2))
    if pvalue <= 0.05:
        change_point_desc = '显著'
    else:
        change_point_desc = '不显著'
    #Pettitt_result = {'突变点位置':K,'突变程度':change_point_desc}
    return K #,Pettitt_result

d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx', sheet_name='Sheet3')
inputdata = d['咸阳年径流']
year=d['年']

print(year[Pettitt_change_point_detection(inputdata)])