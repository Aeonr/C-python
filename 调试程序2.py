import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
# 多数据并列柱状图
bar_width = 0.35
tick_label = ['A', 'B', 'C', 'D', 'E']
plt.bar(x, y, bar_width, align='center', color='#66c2a5', label='班级A')
plt.bar(x + bar_width, y1, bar_width, align='center', color='#8da0cb', label='班级B')
plt.xlabel('测试难度')
plt.ylabel('试卷份数')
plt.xticks(x + bar_width / 2, tick_label)
plt.legend()
plt.show()