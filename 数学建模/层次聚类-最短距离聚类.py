import numpy as np
from sklearn import preprocessing as pp
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

a = np.loadtxt("E:\\python\\数学建模\\模拟数据\\层次聚类模拟数据.txt")
b = pp.minmax_scale(a.T)  # 数据规范化
d = sch.distance.pdist(b)
dd = sch.distance.squareform(d)  # 转成矩阵格式
z = sch.linkage(d)
print(z)
s = [str(i + 1) for i in range(7)]
plt.rc('font', size=16)
sch.dendrogram(z, labels=s)
plt.show()  # 画聚类图
