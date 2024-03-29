import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso, LassoCV
from scipy.stats import zscore

matplotlib.use('TkAgg')
plt.rc('font', size=16)
a = np.loadtxt("E:\\python\\数学建模\\模拟数据\\岭回归和LASSO回归模拟数据.txt")
n = a.shape[1] - 1
aa = zscore(a)
x = aa[:, :n]
y = aa[:, n]
b = []
kk = np.logspace(-4, 0, 100)
for k in kk:
    md = Lasso(alpha=k).fit(x, y)
    b.append(md.coef_)
st = ['s-r', '*-k', 'p-b']
for i in range(3):
    plt.plot(kk, np.array(b)[:, i], st[i])
    plt.legend(['$x_1$', '$x_2$', '$x_3$'], fontsize=15)
    plt.show()
mdcv = LassoCV(alphas=np.logspace(-4, 0, 100)).fit(x, y)
print("最优alpha_：", mdcv.alpha_)
md0 = Lasso(0.21).fit(x, y)
cs0 = md0.coef_
print("回归系数：", cs0)
mu = np.mean(a, axis=0)
s = np.std(a, axis=0, ddof=1)  # 计算均值和标准差
params = [mu[-1] - s[-1] * sum(cs0 * mu[:-1] / s[:-1]), s[-1] * cs0 / s[:-1]]
print("原数据回归系数：", params)
print("拟合优度：", md0.score(x, y))
