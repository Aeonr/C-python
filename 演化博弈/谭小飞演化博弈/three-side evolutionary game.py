# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:09:33 2022
说明：
（1）以下代码基于python3经过pycharm2021、Spyder的运行。
（2）如果运行后没有弹出图片窗口，对于Spyder：tools->preferences->ipython console->graphics->backend->Qt5;
    对于pycharm：file->settings->python scientific->show plot in tool window。
（3）出图后点击图片窗口的configure subplots，可以调整图片的大小等。
@author: 谭小飞同学
"""

# 一幅图的制作，需要导入包+复制动态方程组+参数赋值与plot函数#

# 导入必要的包
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d

# 定义字体防止图象中的字体显示为方框
plt.rcParams['font.sans-serif'] = ['STSong']
# plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# %%复制动态方程组
def yaopin(Fx, t, Rp, Cph, Cpl, Cp, Bt, Fp, Mp, Ct, Ft, Mt, Cg, Tg):
    x, y, z = Fx.tolist()
    return x * (x - 1) * (Cph - Cpl - Cp - Bt - y * (Rp - Bt) - z * (Fp + Mp)), \
           y * (y - 1) * ((1 - x) * (Bt - Mt) - (Ft + Mt) * z - Ct), \
           z * (z - 1) * (Cg - Fp - Ft - Tg + (Mp + Fp + Tg) * x + (Mt + Ft + Tg) * y - Tg * x * y)


# %% 图5
# 防止图片窗口刷屏，只需本次操作，后面无需
plt.close("all")
# 定义一个图象窗口
fig = plt.figure()
# 定义一个三维坐标系
ax = fig.add_subplot(projection='3d')
# 时间或演化次数，从0开始，到50结束，步长0.005，步长越大则图象越粗糙，线条上的标记点越少。
t = np.arange(0, 50, 0.005)
# 定义除t,x,y,z之外的其他参数，对应于前面定义的函数依次是依次是Rp,Cph,Cpl,Cp,Bt,Fp,Mp,Ct,Ft,Mt,Cg,Tg
args = (100, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
# 根据ode函数代入参数x,y,z,t,其他参数，求解方程组yaopin。
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
# 画出x,y,z组成的图象，以红色加号显示
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
# 更换参数Rp，再画一条
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
# 更换参数Rp，再画一条
args = (200, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')

'''
python常用颜色：b蓝色，g绿色，r红色，c青色，m品红色，y黄色，k黑色，w白色；
python常用线型：-实线，:点线，--虚线，-.点横线；
python常用点符号：.实心点，0（字母）小圆圈，v^><四种三角形，s方形，p五角星，*星号，h六芒星，+加号，X叉号，D菱形。
'''
# 不显示网格
# ax.grid(False)
# 三维图视角
ax.view_init(elev=20, azim=-130)
# 图象白底（但仍是灰底）
ax.set_facecolor('w')
# 三维图各轴的标签，可调整至刻度轴的距离
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
# 三维图各轴的刻度区间范围
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
# 图例，可调整位置
plt.legend(labels=('$R_p$=100', '$R_p$=150', '$R_p$=200'), loc=(0.7, 0.5))
# 标题
plt.title("图５ 药品销售收入的影响", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
# 三维图各轴的刻度间隔，这里是从0.2开始，到1.01结束，步长间隔0.2。如果设到1.0结束则图象不显示数字1.0。
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
# 三维图的z轴比较麻烦
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################5小图#####################5小图####################5小图####################
# 定义小图的坐标系，确定其左边，下边位置，宽度，高度
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
# 因为图5的小图是为了显示Rp参数变化的影响，那么只需更改args中的Rp，其他如t、x、y、z保持不变
args = (100, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
# 求解方程
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
# 论文中小图显示x,z，注意线条颜色符号等与大图保持一致
ax1.plot(track5[:, 0], track5[:, 2], 'r+')
# 再次更改参数Rp
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
# 再次解方程
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
# 再次作图
ax1.plot(track5[:, 0], track5[:, 2], 'b-')
args = (200, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'g--')
# 小图添加网格
plt.grid()
# 小图白烟色，与大图保持一致
ax1.set_facecolor('whitesmoke')
# 小图的横纵坐标轴刻度，从0开始，到1结束，步长或间隔0.2
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
# 小图的刻度数字隐藏
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
# 小图坐标轴的区间范围
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###最后在图象上添加文本，以弥补原图的不足###
plt.text(0.8, 0.1, s="x", transform=ax1.transAxes, fontsize=15)  # 小图的横轴标签
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)  # 小图的纵轴标签
# 配合大图中的plt.xticks和plt.yticks，将大图中坐标原点的两个0变为一个0
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
# 如果想改变大图标签z的位置，运行下面这句文本函数即可
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
# 显示图象
plt.show()

# %% 图6#
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
#
args = (150, 85, 0, 10, 20, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
#
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
#
args = (150, 85, 0, 10, 60, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')
# ax.grid(False)
ax.view_init(elev=20, azim=-130)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
#
plt.legend(labels=('$B_t$=20', '$B_t$=40', '$B_t$=60'), loc=(0.7, 0.5))
#
plt.title("图6 寻租成本的影响", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################6小图#####################6小图####################6小图####################
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
###
args = (150, 85, 0, 10, 20, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 0], track5[:, 1], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 0], track5[:, 1], 'b-')
###
args = (150, 85, 0, 10, 60, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 0], track5[:, 1], 'g--')
plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###
plt.text(0.8, 0.1, s="x", transform=ax1.transAxes, fontsize=15)
###
plt.text(0.1, 0.8, s="y", transform=ax1.transAxes, fontsize=15)
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
plt.show()

# %% 图7############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 0, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 40, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')
# ax.grid(False)
ax.view_init(elev=20, azim=-130)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
###
plt.legend(labels=('$F_t$=0', '$F_t$=20', '$F_t$=40'), loc=(0.7, 0.5))
###
plt.title("图7 政府对第三方检测机构罚款额的影响", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################7小图#####################7小图####################7小图####################
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 0, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 40, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'g--')
plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###
plt.text(0.8, 0.1, s="y", transform=ax1.transAxes, fontsize=15)
###
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
plt.show()

# %% 图8############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 0, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 30, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')
# ax.grid(False)
ax.view_init(elev=20, azim=-140)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
###
plt.legend(labels=('$M_t$=0', '$M_t$=15', '$M_t$=30'), loc=(0.7, 0.5))
###
plt.title("图8 政府对第三方检测机构奖励的影响", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################7小图#####################7小图####################7小图####################
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 0, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 30, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'g--')
plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###
plt.text(0.7, 0.1, s="y", transform=ax1.transAxes, fontsize=15)
###
plt.text(0.01, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.58, 0.01, s="0", transform=ax.transAxes, fontsize=10)
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
plt.show()

# %% 图9############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
###
args = (150, 85, 0, 10, 40, 40, 0, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 40, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')
# ax.grid(False)
ax.view_init(elev=20, azim=-130)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
###
plt.legend(labels=('$M_p$=0', '$M_p$=20', '$M_p$=40'), loc=(0.7, 0.5))
###
plt.title("图9 政府对药品生产企业奖励的影响图", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################7小图#####################7小图####################7小图####################
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
###
args = (150, 85, 0, 10, 40, 40, 0, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 40, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'g--')
plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###
plt.text(0.8, 0.1, s="y", transform=ax1.transAxes, fontsize=15)
###
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
plt.show()

# %% 图10############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 20)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 70)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')
# ax.grid(False)
ax.view_init(elev=20, azim=-150)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
###
plt.legend(labels=('$T_g$=20', '$T_g$=40', '$T_g$=70'), loc=(0.7, 0.5))
###
plt.title("图10 政府监管不力遭受的行政处罚的影响", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))
###################7小图#####################7小图####################7小图####################
left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 20)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'r+')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'b-')
###
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 70)
track5 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
###
ax1.plot(track5[:, 1], track5[:, 2], 'g--')
plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
###
plt.text(0.8, 0.1, s="y", transform=ax1.transAxes, fontsize=15)
###
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.65, 0.03, s="0", transform=ax.transAxes, fontsize=10)
# plt.text(0, 0.8, s=r"$z$", transform=ax.transAxes,fontsize=10)
plt.show()

# %% 图11############################################################################
# 定义一个图象窗口
fig = plt.figure()
# 定义一个坐标系
ax = fig.add_subplot(projection='3d')
# 时间或者说演化次数，从0开始，步长0.005，到50结束，步长越小图象越平滑，线条上的标记点越多。
t = np.arange(0, 50, 0.005)
# 除时间t，主体博弈概率xyz之外的其他参数，注意按照顺序依次是Rp,Cph,Cpl,Cp,Bt,Fp,Mp,Ct,Ft,Mt,Cg,Tg，顺序在定义函数时决定。
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
# 嵌套循环，python的缩进需要注意。
for i in np.arange(0.1, 1, 0.2):
    for j in np.arange(0.1, 1, 0.2):
        for k in np.arange(0.1, 1, 0.2):
            # 根据ode代入参数求解方程
            track11 = odeint(yaopin, (i, j, k), t, args)
            # 制图，图象的线型，颜色，点标记符。
            ax.plot(track11[:, 0], track11[:, 1], track11[:, 2])
            # ax.plot(track11[:,0],track11[:,1],track11[:,2],'rD',markevery=5,markerfacecolor="None")
# 循环结束后，先调整图象视角
ax.view_init(elev=25, azim=-45)
# 设置图象白底，但是仍然是灰色
ax.set_facecolor('w')
# 设置各轴的标注，可以调整标注至刻度轴的距离
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
# 设置三维图的各轴的刻度区间
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
# 图象标题，可调整位置，大小，加粗（加粗效果不明显）
plt.title("图11 数组1演化50次结果", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
# 显示图象
plt.show()

# %% 图12############################################################################
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
args = (150, 105, 0, 10, 50, 25, 15, 10, 18, 12, 15, 40)
for i in np.arange(0.1, 1, 0.2):
    for j in np.arange(0.1, 1, 0.2):
        for k in np.arange(0.1, 1, 0.2):
            track11 = odeint(yaopin, (i, j, k), t, args)
            ax.plot(track11[:, 0], track11[:, 1], track11[:, 2])
ax.view_init(elev=22, azim=-43)
ax.set_facecolor('w')
ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)
ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)
plt.title("图12 数组2演化50次结果", x=0.5, y=-0.1, fontsize=15, fontweight='bold')
plt.show()

# %%
'''
亲爱的玛卡巴卡，以上是原论文中的图象，那么三方演化博弈还有其他画图吗？
接下来提供x-t,y-t,z-t在同一张图上显示。
咱们继续以图5为例，但作出如下改动，保持Rp=150不变，
改变x,y,z的初始取值依次为(0.2,0.2,0.2),(0.5,0.5,0.5),(0.8,0.8,0.8)。
'''
# 首先我们学习x-t,y-t,z-t在同一张图上显示，但此前先每个显示一遍
# 子图1##############################################################################
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track1 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
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

# 子图2##############################################################################
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track2 = odeint(yaopin, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track2[:, 0], 'co', markevery=2, markerfacecolor="None")
plt.plot(t, track2[:, 1], 'yD', markevery=10)
plt.plot(t, track2[:, 2], 'mx', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.5', 'y=0.5', 'z=0.5'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图2  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

# 子图3##############################################################################
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track3 = odeint(yaopin, (0.8, 0.8, 0.8), t, args)
plt.plot(t, track3[:, 0], 'ch', markevery=2, markerfacecolor="None")
plt.plot(t, track3[:, 1], 'gp', markevery=10)
plt.plot(t, track3[:, 2], 'ks', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.8', 'y=0.8', 'z=0.8'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图3  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()

###现在把上面三张图的线条放在同一张图
# 子图4##############################################################################
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track1 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
track2 = odeint(yaopin, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track2[:, 0], 'co', markevery=2, markerfacecolor="None")
plt.plot(t, track2[:, 1], 'yD', markevery=10)
plt.plot(t, track2[:, 2], 'mx', markevery=10)
track3 = odeint(yaopin, (0.8, 0.8, 0.8), t, args)
plt.plot(t, track3[:, 0], 'ch', markevery=2, markerfacecolor="None")
plt.plot(t, track3[:, 1], 'gp', markevery=10)
plt.plot(t, track3[:, 2], 'ks', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2', 'x=0.5', 'y=0.5', 'z=0.5', 'x=0.8', 'y=0.8', 'z=0.8'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图4  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(False)
plt.show()

# %%接下来，把上面4副子图放在同一个窗口显示。
fig, ax = plt.subplots()

# 子图1
ax1 = plt.subplot(2, 2, 1)
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track1 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))
ax1.set_xlabel("t", labelpad=-5)
ax1.set_ylabel("x0/y0/z0", labelpad=-5)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
plt.grid(True)

##############################################################################
# 子图2
ax2 = plt.subplot(2, 2, 2)
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track2 = odeint(yaopin, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track2[:, 0], 'co', markevery=2, markerfacecolor="None")
plt.plot(t, track2[:, 1], 'yD', markevery=10)
plt.plot(t, track2[:, 2], 'mx', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.5', 'y=0.5', 'z=0.5'))
ax2.set_xlabel("t", labelpad=-5)
ax2.set_ylabel("x0/y0/z0", labelpad=-5)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
plt.grid(True)

##############################################################################
# 子图3
ax3 = plt.subplot(2, 2, 3)
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track3 = odeint(yaopin, (0.8, 0.8, 0.8), t, args)
plt.plot(t, track3[:, 0], 'ch', markevery=2, markerfacecolor="None")
plt.plot(t, track3[:, 1], 'gp', markevery=10)
plt.plot(t, track3[:, 2], 'ks', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.8', 'y=0.8', 'z=0.8'))
ax3.set_xlabel("t", labelpad=-5)
ax3.set_ylabel("x0/y0/z0", labelpad=-5)
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
plt.grid(True)

##############################################################################
# 子图4
ax4 = plt.subplot(2, 2, 4)
t = np.arange(0, 1, 0.001)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track1 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)
plt.plot(t, track1[:, 0], 'r>', markevery=2, markerfacecolor="None")
plt.plot(t, track1[:, 1], 'g*', markevery=10)
plt.plot(t, track1[:, 2], 'b--', markevery=10)
track2 = odeint(yaopin, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track2[:, 0], 'co', markevery=2, markerfacecolor="None")
plt.plot(t, track2[:, 1], 'yD', markevery=10)
plt.plot(t, track2[:, 2], 'mx', markevery=10)
track3 = odeint(yaopin, (0.8, 0.8, 0.8), t, args)
plt.plot(t, track3[:, 0], 'ch', markevery=2, markerfacecolor="None")
plt.plot(t, track3[:, 1], 'gp', markevery=10)
plt.plot(t, track3[:, 2], 'ks', markevery=10)
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2', 'x=0.5', 'y=0.5', 'z=0.5', 'x=0.8', 'y=0.8', 'z=0.8'))
ax4.set_xlabel("t", labelpad=-5)
ax4.set_ylabel("x0/y0/z0", labelpad=-5)
plt.grid(False)
plt.title("图5  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", x=-0.2, y=-0.3)
plt.show()

# %% 平面茎叶图或棉棒图，MATLAB中是火柴棍图stem
fig, ax = plt.subplots()
t = np.arange(0, 1, 0.05)
args = (150, 85, 0, 10, 40, 40, 20, 10, 20, 15, 15, 40)
track1 = odeint(yaopin, (0.2, 0.2, 0.2), t, args)

# linefmt：棉棒的样式;markerfmt：棉棒末端的样式；basefmt：指定基线的样式
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

