import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STSong']
plt.rcParams['axes.unicode_minus'] = False

def DS(Fx, t, a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, f3):
    x, y, z = Fx.tolist()
    return x * (1 - x) * ((d1 * z + e1 * (z - 1)) * (y - 1) - d1 * y + y * (d1 - a1 + f1) + (y - 1) * (a1 - d1 - f1 + (b1 + c1) * (z - 1))), \
           y * (1 - y) * (b2 - a2 + c2 + d2 + f2 + b1 * x - b2 * z - c2 * z + e2 * x - d2 * z - b1 * x * z), \
           z * (1 - z) * (c3 - b3 + d3 + g1 + c1 * x + b2*y + e3*x + f3*y - c1*x*y)
#  基础参数 (15, 10, 5, 5, 10, 20, 10, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
#          (a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, f2, a3, b3, c3, d3, e3, f3, g1)

# 单个参数调整三方演化博弈曲线
plt.close("all")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
args = (10,  5, 20, 10,  6, 10, 30, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
args = (10,  5, 20, 10,  6, 10, 80, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')

ax.view_init(elev=20, azim=-130)
ax.set_facecolor('w')

ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)

ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)

plt.legend(labels=('$c_1$=1000', '$c_1$=1500', '$c_1$=2000'), loc=(0.7, 0.5))
plt.title("图５", x=0.5, y=-0.1, fontsize=15, fontweight='bold')

plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))

left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])

args = (10,  5, 20, 10,  6, 10, 30, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'r+')

args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'b-')

args = (10,  5, 20, 10,  6, 10, 80, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'g--')

plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
plt.text(0.8, 0.1, s="x", transform=ax1.transAxes, fontsize=15)
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
plt.show()

# 单个参数调整一方行为调整的曲线
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.005)
args = (10, 10, 10, 10, 10, 10, 50, 100, 50, 150, 200, 100, 0.7, 0.8, 0.5, 20, 20, 40, 20, 20, 40, 0.1, 0.2, 15, 30, 20, 0.5, 0.4)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 2], 'r-.', markevery=2, markerfacecolor="None")
args = (10, 10, 10, 10, 10, 10, 100, 100, 50, 150, 200, 100, 0.7, 0.8, 0.5, 20, 20, 40, 20, 20, 40, 0.1, 0.2, 15, 30, 20, 0.5, 0.4)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 2], 'b-', markevery=2, markerfacecolor="None")
args = (10, 10, 10, 10, 10, 10, 150, 100, 50, 150, 200, 100, 0.7, 0.8, 0.5, 20, 20, 40, 20, 20, 40, 0.1, 0.2, 15, 30, 20, 0.5, 0.4)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 2], 'g--', markevery=2, markerfacecolor="None")

plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('c1=50', 'c1=100', 'c1=150'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$c1$' + "不同时政府的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

# 数组仿真实验
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.0005)
args = (10, 5, 20, 10, 6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
for i in np.arange(0.1, 1, 0.2):
    for j in np.arange(0.1, 1, 0.2):
        for k in np.arange(0.1, 1, 0.2):
            track4 = odeint(DS, (i, j, k), t, args)
            ax.plot(track4[:, 0], track4[:, 1], track4[:, 2])

ax.view_init(elev=25, azim=-45)
ax.set_facecolor('w')

ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)

ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)

plt.title("图2 数组1演化50次结果", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.show()

# x-t，y-t，z-t图
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track1 = odeint(DS, (0.2, 0.2, 0.2), t, args)

plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))

ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track1 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track1 = odeint(DS, (0.8, 0.8, 0.8), t, args)
plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

# 平面茎叶图
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.05)
args = (10, 10, 10, 10, 10, 10, 100, 100, 50, 150, 200, 100, 0.7, 0.8, 0.5, 20, 20, 40, 20, 20, 40, 0.1, 0.2, 15, 30, 20, 0.5, 0.4)
track1 = odeint(DS, (0.5, 0.5, 0.5), t, args)

plt.stem(t, track1[:, 0], linefmt="r-.", markerfmt="r+", basefmt="r--")
plt.stem(t, track1[:, 1], linefmt="b-.", markerfmt="bo", basefmt="b--")
plt.stem(t, track1[:, 2], linefmt="m-.", markerfmt="m^", basefmt="m--")
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()