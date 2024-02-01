# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:16:33 2022
（1）代码是在pycharm专业版2021、Spyder运行成功的；
（2）本文《农户与企业合作下的农产品质量安全演化博弈仿真研究》；
（3）不含相位图，只是数值仿真模拟；
（4）传统双方演化博弈python代码；
（5）如果运行后没有弹出图片窗口，
对于Spyder：tools->preferences->ipython console->graphics->backend->Qt5;
对于pycharm：file->settings->python scientific->show plot in tool window；
（6）运行代码之前先安装好所有的包并重启；
（7）出图后点击图片窗口的configure subplots，可以调整图片的大小等；
（8）代码详情关注bilibili或者知乎账户：谭小飞同学。
@author: 谭小飞同学
"""
# %% 导入三方包
# pip install numpy
# pip install scipy
# pip install matplotlib
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# %% 复制动态方程组
def nonghu(Fy, t, n, rA, d, beta, fB, miu, alpha, sA, fA, theta, lamda, sB):
    y1, y2 = Fy.tolist()
    return y1 * (1 - y1) * ((1 - n) * (1 + rA) - (1 - y2) * (d - beta * fB * miu) + alpha * (sA + fA) - 1), \
           y2 * (1 - y2) * (y1 * (1 - theta) * (1 + rA) * lamda - miu + beta * (sB + fB) * miu)


# %% 图3 初始仿真实试验结果
# %reset -f
# %clear
plt.close("all")  # 防止刷屏
fig, ax = plt.subplots()
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track[:, 0], 'ks')
plt.plot(t, track[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), loc=1)

ax.set_xlabel("time", labelpad=-10)
ax.set_ylabel("proportion", labelpad=-10)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)
ax.set_title('the proportion')
fig.suptitle('图3 初始仿真实试验结果', x=0.5, y=0.05)
plt.show()
# %% 图4 仿真实试验结果分析1
fig, ax = plt.subplots()
# 子图1
ax1 = plt.subplot(1, 4, 1)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track1 = odeint(nonghu, (0.60, 0.40), t, args)
plt.plot(t, track1[:, 0], 'ks')
plt.plot(t, track1[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)

ax1.set_xlabel("time", labelpad=-10)
ax1.set_ylabel("proportion", labelpad=-10)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 1)
ax1.set_title('the proportion')
plt.text(x=10, y=0.5, s='X=0.60,Y=0.40')
##############################################################################
# 子图2
ax2 = plt.subplot(1, 4, 2)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track2 = odeint(nonghu, (0.50, 0.40), t, args)
plt.plot(t, track2[:, 0], 'ks')
plt.plot(t, track2[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax2.set_xlabel("time", labelpad=-10)
ax2.set_ylabel("proportion", labelpad=-10)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1)
ax2.set_title('the proportion')
plt.text(x=15, y=0.5, s='X=0.50,Y=0.40')
##############################################################################
# 子图3
ax3 = plt.subplot(1, 4, 3)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track3 = odeint(nonghu, (0.56, 0.45), t, args)
plt.plot(t, track3[:, 0], 'ks')
plt.plot(t, track3[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax3.set_xlabel("time", labelpad=-10)
ax3.set_ylabel("proportion", labelpad=-10)
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 1)
ax3.set_title('the proportion')
plt.text(x=20, y=0.5, s='X=0.56,Y=0.45')
##############################################################################
# 子图4
ax4 = plt.subplot(1, 4, 4)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track4 = odeint(nonghu, (0.56, 0.35), t, args)
plt.plot(t, track4[:, 0], 'ks')
plt.plot(t, track4[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax4.set_xlabel("time", labelpad=-10)
ax4.set_ylabel("proportion", labelpad=-10)
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 1)
ax4.set_title('the proportion')
plt.text(x=20, y=0.5, s='X=0.56,Y=0.35')
fig.suptitle('图4 仿真实试验结果分析1', x=0.5, y=0.05)
plt.show()

# %% 图5 仿真实试验结果分析2
fig, ax = plt.subplots()
# 子图1
ax1 = plt.subplot(1, 4, 1)
t = np.arange(0, 100, 1)
args = (0.05, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.05, 0.1, 0.25)
track1 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track1[:, 0], 'ks')
plt.plot(t, track1[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax1.set_xlabel("time", labelpad=-10)
ax1.set_ylabel("proportion", labelpad=-10)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 1)
ax1.set_title('the proportion')
plt.text(x=10, y=0.5, s=r'$\eta=0.05,\theta=0.05$')
##############################################################################
# 子图2
ax2 = plt.subplot(1, 4, 2)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.15, 0.5, 0.25, 0.25, 0.15, 0.1, 0.25)
track2 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track2[:, 0], 'ks')
plt.plot(t, track2[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax2.set_xlabel("time", labelpad=-10)
ax2.set_ylabel("proportion", labelpad=-10)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1)
ax2.set_title('the proportion')
plt.text(x=15, y=0.5, s=r'$\mu=0.15,\theta=0.15$')
##############################################################################
# 子图3
ax3 = plt.subplot(1, 4, 3)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.6, 0.3, 0.1, 0.6, 0.3, 0.3, 0.1, 0.1, 0.3)
track3 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track3[:, 0], 'ks')
plt.plot(t, track3[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax3.set_xlabel("time", labelpad=-10)
ax3.set_ylabel("proportion", labelpad=-10)
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 1)
ax3.set_title('the proportion')
plt.text(x=20, y=0.5, s=r'$\alpha=\beta=0.6$' + '\n' + '$S_{A}=F_{A}=0.3$' + '\n' + '$S_{B}=F_{B}=0.3$')
##############################################################################
# 子图4
ax4 = plt.subplot(1, 4, 4)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.4, 0.2, 0.1, 0.4, 0.2, 0.2, 0.1, 0.1, 0.2)
track4 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track4[:, 0], 'ks')
plt.plot(t, track4[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax4.set_xlabel("time", labelpad=-10)
ax4.set_ylabel("proportion", labelpad=-10)
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 1)
ax4.set_title('the proportion')
plt.text(x=20, y=0.5, s=r'$\alpha=\beta=0.4$' + '\n' + '$S_{A}=F_{A}=0.2$' + '\n' + '$S_{B}=F_{B}=0.2$')
fig.suptitle('图5 仿真实试验结果分析2', x=0.5, y=0.05)
plt.show()

# %%图6 仿真实试验结果分析3
fig, ax = plt.subplots()
# 子图1
ax1 = plt.subplot(1, 4, 1)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 0.75, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track1 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track1[:, 0], 'ks')
plt.plot(t, track1[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax1.set_xlabel("time", labelpad=-10)
ax1.set_ylabel("proportion", labelpad=-10)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 1)
ax1.set_title('the proportion')
plt.text(x=10, y=0.5, s='i=0.05,d=0.75')
##############################################################################
# 子图2
ax2 = plt.subplot(1, 4, 2)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1.25, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track2 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track2[:, 0], 'ks')
plt.plot(t, track2[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax2.set_xlabel("time", labelpad=-10)
ax2.set_ylabel("proportion", labelpad=-10)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1)
ax2.set_title('the proportion')
plt.text(x=15, y=0.5, s='i=1.5,d=1.25')
##############################################################################
# 子图3
ax3 = plt.subplot(1, 4, 3)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.1, 0.5, 0.25, 0.25, 0.1, 0.15, 0.25)
track3 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track3[:, 0], 'ks')
plt.plot(t, track3[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax3.set_xlabel("time", labelpad=-10)
ax3.set_ylabel("proportion", labelpad=-10)
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 1)
ax3.set_title('the proportion')
plt.text(x=20, y=0.5, s=r'$\lambda=0.15,\mu=0.10$')
##############################################################################
# 子图4
ax4 = plt.subplot(1, 4, 4)
t = np.arange(0, 100, 1)
args = (0.1, 0.5, 1, 0.5, 0.25, 0.15, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25)
track4 = odeint(nonghu, (0.56, 0.40), t, args)
plt.plot(t, track4[:, 0], 'ks')
plt.plot(t, track4[:, 1], 'ro')
# 以下两行保证title中的汉字能够正常显示而非方框
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(np.arange(0, 101, step=100))
plt.yticks(np.arange(0, 1.1, step=1))
plt.legend(labels=('X', 'Y'), bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
ax4.set_xlabel("time", labelpad=-10)
ax4.set_ylabel("proportion", labelpad=-10)
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 1)
ax4.set_title('the proportion')
plt.text(x=20, y=0.5, s=r'$\lambda=0.10,\mu=0.15$')
fig.suptitle('图6 仿真实试验结果分析3', x=0.5, y=0.05)
plt.show()
