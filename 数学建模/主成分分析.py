import numpy as np
from sklearn.decomposition import PCA

a = np.loadtxt("..\\数学建模\\模拟数据\\主成分分析模拟数据.txt")
b = np.r_[a[:, 1:4], a[:, -3:]]
md = PCA().fit(b)  # 构造并训练模型
print("特征值为：", md.explained_variance_)
print("各主成分的贡献率：", md.explained_variance_ratio_)
print("奇异值：", md.singular_values_)
print("各主成分的系数：\n", md.components_)
# 后面为与库函数进行对比
cf = np.cov(b.T)  # 计算协方差阵
c, d = np.linalg.eig(cf)  # 求特征值和特征向量
print("特征值为：", c)
print("特征向量为：\n", d)
print("各主成分贡献率为：", c / np.sum(c))
