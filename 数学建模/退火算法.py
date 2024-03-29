import matplotlib
from numpy import loadtxt, sin, cos, inf, exp
from numpy import array, r_, c_, arange
from numpy.lib.scimath import arccos
from numpy.random import shuffle, randint, rand
from matplotlib.pyplot import plot, show, rc

matplotlib.use('TkAgg')  # 用于修复“module 'backend_interagg' has no attribute 'FigureCanvas'. Did you mean: 'FigureCanvasAgg'”?
a = loadtxt("E:\\python\\数学建模\\模拟数据\\退火算法与遗传算法模拟数据.txt")
x = a[:, ::2].flatten()
y = a[:, 1::2].flatten()
d1 = array([[0, 0]])
xy = c_[x, y]
xy = r_[d1, xy, d1]
N = xy.shape[0]
d = array([[6370 * arccos(cos(xy[i, 0] - xy[j, 0]) * cos(xy[i, 1]) * cos(xy[j, 1]) + sin(xy[i, 1]) * sin(xy[j, 1])) for
            i in range(N)] for j in range(N)]).real
path = arange(N)
L = inf
for j in range(1000):
    path0 = arange(1, N - 1)
    shuffle(path0)
    path0 = r_[0, path0, N - 1]
    L0 = d[0, path0[1]]
    for i in range(1, N - 1):
        L0 += d[path0[i], path0[i + 1]]
    if L0 < L:
        path = path0
        L = L0
print(path, '\n', L)
e = 0.1 ** 30
M = 20000
at = 0.999
T = 1
for k in range(M):
    c = randint(1, 21, 2)
    c.sort()
    c1 = c[0]
    c2 = c[1]
    df = d[path[c1 - 1], path[c2]] + d[path[c1], path[c2 + 1]] - d[path[c1 - 1], path[c1]] - d[path[c2], path[c2 + 1]]
    if df < 0:
        path = r_[path[0], path[1:c1], path[c2:c1 - 1:-1], path[c2 + 1:22]]
        L = L + df
    else:
        if exp(-df / T) >= rand(1):
            path = r_[path[0], path[1:c1], path[c2:c1 - 1:-1], path[c2 + 1:22]]
            L = L + df
    T = T * at
    if T < e: break
print(path, '\n', L)
xx = xy[path, 0]
yy = xy[path, 1]
rc('font', size=16)
plot(xx, yy, '-*')
show()
