import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STSong']
plt.rcParams['axes.unicode_minus'] = False

def DS(Fx, t, a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2,f2, a3, b3, c3, d3, e3, f3, g1):
    x, y, z = Fx.tolist()
    return x * (1 - x) * ((d1 * z + e1 * (z - 1)) * (y - 1) - d1 * y + y * (d1 - a1 + f1) + (y - 1) * (a1 - d1 - f1 + (b1 + c1) * (z - 1))), \
           y * (1 - y) * (b2 - a2 + c2 + d2 + f2 + b1 * x - b2 * z - c2 * z + e2 * x - d2 * z - b1 * x * z), \
           z * (1 - z) * (c3 - b3 + d3 + g1 + c1 * x + b2*y + e3*x + f3*y - c1*x*y)
#  基础参数 (15, 10, 5, 5, 10, 20, 10, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
#          (a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, f2, a3, b3, c3, d3, e3, f3, g1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.05)
args = (15, 10, 5, 5, 10, 20, 10, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
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

plt.title("图1 参数演化50次结果", x=0.5, y=-0.1, fontsize=15, fontweight='bold')

plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 300

plt.show()