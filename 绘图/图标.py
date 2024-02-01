import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("C:\\Users\\CYH10\\Desktop\\BI.xlsx")
print(data.head())

x = np.arange(3)
y1 = data["BMI_mean"]
y2 = data["overweight"]
y3 = data["obesity"]

bar_width = 0.35
tick_label = ['陕北', '汉中', '陕南']

plt.bar(x, y1, 0.25, align='center', color='#66c2a5', label='地区平均BMI')
plt.bar(x + 0.25, y2, 0.25, align='center', color='#8da0cb', label='地区超重人数')
plt.bar(x + 2*0.25, y3, 0.25, align='center', color='#8da4cb', label='地区肥胖人数')
plt.xlabel('地区', fontsize=10)
plt.xticks(x + 2*bar_width / 2, tick_label)
plt.xticks(fontsize=10)
plt.legend()
plt.text()
plt.savefig("myimage1.png", dpi=1200)
plt.show()
