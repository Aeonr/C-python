import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
mean=np.array([[-2 , -2],[2, 2] , [6 ,6]])
cov=np.array([[[0.3, 0], [0 , 0.3]] , [[0.4 , 0] , [0 , 0.4]] , [[0.5 , 0] ,[0 , 0.5]]])
x0=[]
y0=[]
for i in range(3):
    x,y=np.random.multivariate_normal(mean[i],cov[i],1000).T
    x0=np.hstack([x0,x])    #np.hstack将矩阵按顺序叠加
    y0=np.hstack([y0,y])
plt.rc('font',size=16)
plt.rc('font',family='SimHei')
plt.rc('axes',unicode_minus=False)
plt.subplots(121)
plt.scatter(x0,y0,marker='.')
X=np.vstack([x0,y0]).T
np.save('k值聚类模拟数据.npy',X)
TSSE=[]
K=10
for k in range(1,K+1):
    SSE=[]
    md=KMeans(n_clusters=k)
    md.fit(X)
    labels=md.labels_
    centers=md.cluster_centers_
    for label in set(labels):
        SSE.append(np.sum((X[labels==label,:]-centers[label,:])**2))
    TSSE.append(np.sum(SSE))
plt.subplots(122)
plt.style.use('ggplot')
plt.plot(range(1,K+1),TSSE,'b*-')
plt.xlabel('簇的个数')
plt.ylabel('簇内离差平方和')
plt.show()