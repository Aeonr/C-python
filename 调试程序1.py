import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 模型参数
r_P, K_P = 0.1, 200
r_H, K_H = 0.05, 100
r_C, K_C = 0.02, 50

a_PH, a_PC = 0.01, 0.02
b_HP, a_HC = 0.02, 0.01
b_CP, b_CH = 0.01, 0.03

m_P, m_H, m_C = 0.005, 0.005, 0.005
e = 0.1
d_E = 0.02

alpha_P, alpha_H, alpha_C = 0.001, 0.002, 0.003

# 初始种群数量和环境资源
initial_population = [150, 80, 20, 1000]  # 初始植物、食草动物、食肉动物数量，初始环境资源数量为1000

# 时间点
time_points = np.linspace(0, 500, 1000)

# 社会-生态系统动力学模型方程
def model(populations, t):
    P, H, C, E = populations
    dPdt = r_P * P * (1 - P / K_P) - a_PH * P * H - a_PC * P * C - m_P * P
    dHdt = r_H * H * (1 - H / K_H) - b_HP * H * P - a_HC * H * C - m_H * H
    dCdt = r_C * C * (1 - C / K_C) - b_CP * C * P - b_CH * C * H - m_C * C
    dEdt = e - d_E * E - alpha_P * P**2 - alpha_H * H**2 - alpha_C * C**2
    return [dPdt, dHdt, dCdt, dEdt]

# 求解微分方程
populations = odeint(model, initial_population, time_points)

# 绘制结果
plt.figure(figsize=(15, 10))
plt.plot(time_points, populations[:, 0], label='植物')
plt.plot(time_points, populations[:, 1], label='食草动物')
plt.plot(time_points, populations[:, 2], label='食肉动物')
plt.plot(time_points, populations[:, 3], label='环境资源')
plt.title('社会-生态系统动力学模型')
plt.xlabel('时间')
plt.ylabel('种群数量/环境资源')
plt.legend()
plt.show()
