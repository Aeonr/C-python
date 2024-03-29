import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge,RidgeCV
from scipy.stats import zscore
import matplotlib
matplotlib.use('TkAgg')
a=np.loadtxt("E:\\python\\数学建模\\模拟数据\\岭回归和LASSO回归模拟数据.txt")
n=a.shape[1]-1 #自变量个数
aa=zscore(a) #数据标准化
x=aa[:,:n]
y=aa[:,n]
b=[]
kk=np.logspace(-4,0,100)
for i in kk:
    md=Ridge(alpha=i).fit(x,y)
    b.append(md.coef_)
print(b)
st=['s-r','*-k','p-b']
for i in range(3):
    plt.plot(kk,np.array(b)[:,i],st[i])
    plt.legend(['$x_1$','$x_2$','$x_3$'],fontsize=15)
    plt.show()
mdcv=RidgeCV(alphas=np.logspace(-4,0,100)).fit(x,y)
print(mdcv.alpha_)
md0=Ridge(0.4).fit(x,y)   #构建拟合模型  k=0.4 实际建模时mdcv.alpha_为最佳k值
cs0=md0.coef_   #提出相关系数
print(cs0)
mu=np.mean(a,axis=0)
s=np.std(a,axis=0,ddof=1)#计算均值和标准差
params=[mu[-1]-s[-1]*sum(cs0*mu[:-1]/s[:-1]),s[-1]*cs0/s[:-1]]
print("原数据回归系数：",params)
print("拟合优度：",md0.score(x,y))