import numpy as np
import scipy.cluster.hierarchy as sch
from sklearn import preprocessing as pp
import matplotlib.pyplot as plt

a = np.loadtxt("E:\\python\\数学建模\\模拟数据\\层次聚类模拟数据.txt")
b = pp.minmax_scale(a.T)
d = sch.distance.pdist(b)
z = sch.linkage(d, 'complete')
print(z)
s = [str(i + 1) for i in range(7)]
plt.rc('font', size=16)
sch.dendrogram(z, labels=s)
plt.show()
