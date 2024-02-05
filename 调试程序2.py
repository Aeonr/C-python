import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("C:\\Users\\CYH10\\Desktop\\灵敏度分析.xlsx")

env = data['env']
rm = data['rm']
rf = data['rf']
a = data['a']
b = data['b']

p1 = np.polyfit(env, rm, deg=1)
plt.plot(env, np.polyval(p1, env), label="rm")
p2 = np.polyfit(env, rf, deg=1)
plt.plot(env, np.polyval(p2, env), label="rf")
p3 = np.polyfit(env, a, deg=1)
plt.plot(env, np.polyval(p3, env), label="a")
p4 = np.polyfit(env, b, deg=1)
plt.plot(env, np.polyval(p4, env), label="b")
plt.legend()
plt.show()