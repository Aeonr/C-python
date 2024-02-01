import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')
a=np.loadtxt("E:\\python\数学建模\\模拟数据\\多元线性回归模拟数据.txt")
x=a[:,0]
y=a[:,1]
z=a[:,2]
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x,y,z)
ax.set_xlabel('sepal length (cm)', fontdict={'size': 10, 'color': 'black'})
ax.set_ylabel('sepal width (cm)', fontdict={'size': 10, 'color': 'black'})
ax.set_zlabel('petal length (cm)', fontdict={'size': 10, 'color': 'black'})
plt.show()