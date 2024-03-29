import numpy as np
from scipy.stats import zscore

a = np.loadtxt("E:\\python\\数学建模\\模拟数据\\主成分分析应用模拟数据.txt")
print("相关系数矩阵：\n", np.corrcoef(a.T))
b = np.delete(a, 0, axis=1)  # 删除第一列数据,用第二个指标控制
c = zscore(b)
r = np.corrcoef(c.T)
d, e = np.linalg.eig(r)
rate = d / d.sum()  # 计算各主成分贡献率
print("特征值为：", d)
print("特征向量：\n", e)
print("各主成分贡献率：", rate)
k = 1  # 提取主成分个数
F = e[:, :k]
score_mat = c.dot(F)  # 计算主成分得分矩阵
score1 = score_mat.dot(rate[0:k])  # 计算各评价对象得分
score2 = -score1  # 调整得分的正负,可要可不要
print("各评价对象得分：", score2)
index = score1.argsort() + 1  # 排序后每个元素在原数组中的位置
print("各城市标号排序：", index)
