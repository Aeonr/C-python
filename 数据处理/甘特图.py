import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换sans-serif字体
# plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

plt.barh(y=1, width=1, height=0.5, left=0, edgecolor='white', color='#8CD77F')
plt.barh(y=2, width=1, height=0.5, left=1, edgecolor='white', color='#B1DFE7')
plt.barh(y=3, width=1, height=0.5, left=2, edgecolor='white', color='#B9E9C8')
plt.barh(y=4, width=1, height=0.5, left=3, edgecolor='white', color='#AEC4E5')
plt.barh(y=5, width=1, height=0.5, left=4, edgecolor='white', color='#D28670')
plt.barh(y=6, width=1, height=0.5, left=5, edgecolor='white', color='#D9D9D9')


# y轴坐标显示
plt.yticks([1, 2, 3, 4, 5, 6], ['论文开题', '文献梳理', '数据处理', '实证分析', '论文撰写', '论文修改'])
# x轴坐标显示
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['2024.10.16', '2024.10.29', '2024.12.15', '2025.01.15', '2025.02.15', '2025.03.20', '2025.05.30'])
plt.xticks(fontsize=9)

plt.grid(axis='x', linestyle='--', linewidth=0.5, alpha=0.5)
plt.show()
