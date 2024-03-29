# from scipy import stats
# import numpy as np
# from matplotlib import pyplot as plt
# import pandas as pd
#
# def sk(data):
#     n = len(data)
#     Sk = [0]
#     UFk = [0]
#     s = 0
#     E = [0]
#     Var = [0]
#     for i in range(1, n):
#         for j in range(i):
#             if data[i] > data[j]:
#                 s = s + 1
#             else:
#                 s = s + 0
#         Sk.append(s)
#         E.append((i + 1) * (i + 2) / 4)  # Sk[i]的均值
#         Var.append((i + 1) * i * (2 * (i + 1) + 5) / 72)  # Sk[i]的方差
#         UFk.append((Sk[i] - E[i]) / np.sqrt(Var[i]))
#
#     UFk = np.array(UFk)
#     return UFk
#
#
# # a为置信度
# def MK(data, a):
#     ufk = sk(data)  # 顺序列
#     print(ufk)
#     ubk1 = sk(data[::-1])  # 逆序列
#     ubk = -ubk1[::-1]  # 逆转逆序列
#     print(ubk)
#     # 输出突变点的位置
#     p = []
#     u = ufk - ubk
#     for i in range(1, len(ufk)):
#         if u[i - 1] * u[i] < 0:
#             p.append(i)
#     if p:
#         print("突变点位置：", p)
#     else:
#         print("未检测到突变点")
#
#     # 画图
#     conf_intveral = stats.norm.interval(a, loc=0, scale=1)  # 获取置信区间
#
#     plt.figure(figsize=(10, 5))
#     plt.plot(range(len(data)), ufk, label='UFk', color='r')
#     plt.plot(range(len(data)), ubk, label='UBk', color='b')
#     plt.ylabel('UFk-UBk', fontsize=25)
#     x_lim = plt.xlim()
#     plt.ylim([-6, 7])
#     plt.plot(x_lim, [conf_intveral[0], conf_intveral[0]], color='r', linestyle='--',  label='95%显著区间')
#     plt.plot(x_lim, [conf_intveral[1], conf_intveral[1]], color='r', linestyle='--')
#     plt.axhline(0, ls="--", c="k")
#     plt.legend(loc='upper center', frameon=False, ncol=3, fontsize=20)  # 图例
#     plt.xticks(fontsize=25)
#     plt.yticks(fontsize=25)
#     plt.rcParams['font.sans-serif'] = ['KaiTi']
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.show()
#
# d = pd.read_excel('E:\\建模比赛\\林家村日径流深1970-2014.xlsx', sheet_name='年径流量')
# data = d['年径流']
#
# # d = pd.read_excel('E:\\建模比赛\\林家村月均流量资料.xls',sheet_name='Sheet2')
# # data = d['径流量'][0:74]
# # year = d['年份'][0:74]
#
# # 输入数据和置信度即可
# MK(data, 0.95)



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def Kendall_change_point_detection(inputdata):
    inputdata = np.array(inputdata)
    n=inputdata.shape[0]
    # 正序列计算---------------------------------
    # 定义累计量序列Sk，初始值=0
    Sk = [0]
    # 定义统计量UFk，初始值 =0
    UFk = [0]
    # 定义Sk序列元素s，初始值 =0
    s = 0
    Exp_value = [0]
    Var_value = [0]
    # i从1开始，因为根据统计量UFk公式，i=0时，Sk(0)、E(0)、Var(0)均为0
    # 此时UFk无意义，因此公式中，令UFk(0)=0
    for i in range(1,n):
        for j in range(i):
            if inputdata[i] > inputdata[j]:
                s = s+1
            else:
                s = s+0
        Sk.append(s)
        Exp_value.append((i+1)*(i+2)/4 )                     # Sk[i]的均值
        Var_value.append((i+1)*i*(2*(i+1)+5)/72 )            # Sk[i]的方差
        UFk.append((Sk[i]-Exp_value[i])/np.sqrt(Var_value[i]))
    # ------------------------------正序列计算
    # 逆序列计算---------------------------------
    # 定义逆序累计量序列Sk2，长度与inputdata一致，初始值=0
    Sk2 = [0]
    # 定义逆序统计量UBk，长度与inputdata一致，初始值=0
    UBk = [0]
    UBk2 = [0]
    # s归0
    s2 =  0
    Exp_value2 = [0]
    Var_value2 = [0]
    # 按时间序列逆转样本y
    inputdataT = list(reversed(inputdata))
    # i从2开始，因为根据统计量UBk公式，i=1时，Sk2(1)、E(1)、Var(1)均为0
    # 此时UBk无意义，因此公式中，令UBk(1)=0
    for i in range(1,n):
        for j in range(i):
            if inputdataT[i] > inputdataT[j]:
                s2 = s2+1
            else:
                s2 = s2+0
        Sk2.append(s2)
        Exp_value2.append((i+1)*(i+2)/4 )                     # Sk[i]的均值
        Var_value2.append((i+1)*i*(2*(i+1)+5)/72 )            # Sk[i]的方差
        UBk.append((Sk2[i]-Exp_value2[i])/np.sqrt(Var_value2[i]))

        UBk2.append(-UBk[i])

    UBkT = list(reversed(UBk2))
    diff = np.array(UFk) - np.array(UBkT)
    K = list()
    # 找出交叉点
    for k in range(1,n):
        if diff[k-1]*diff[k]<0:
            K.append(year[k])
    # 做突变检测图时，使用UFk和UBkT
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n+1), UFk, label='UFk') # UFk
    plt.plot(range(1, n+1), UBkT, label='UBk') # UBk
    plt.ylabel('UFk-UBk')
    x_lim = plt.xlim()
    plt.plot(x_lim, [-1.96,-1.96],'--',color='r')
    plt.plot(x_lim, [  0  ,  0  ],'--')
    plt.plot(x_lim, [+1.96,+1.96],'--',color='r')
    plt.legend(loc=2) # 图例
    plt.show()
    return K

d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx', sheet_name='Sheet3')
inputdata = d['咸阳年径流']
year=d['年']

print(Kendall_change_point_detection(inputdata))