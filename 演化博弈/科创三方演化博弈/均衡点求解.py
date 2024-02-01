from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

j = open('E:\\科创\\均衡点.txt', 'w')

# 定义符号 symbol
x, y, z = sp.symbols('x,y,z')  # 决策变量

# 参数
example = 'a1,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,a3,b3,c3,d3,e3,f3'
param_list = example.split(',')
for param in param_list:
    exec(f"{param}=sp.symbols('{param}')")

# 复制动态方程
fx = x * (1 - x) * ((y - 1) * (a1 - d1 + (b1 + c1) * (z - 1)) - d1 * y + (d1 * z + e1 * (z - 1)) * (y - 1) + y * (d1 - a1 + f1))
fy = - y * (1 - y) * (z * (c2 + f1) + (z - 1) * (d2 + b1 * x - f1 * x) + (z - 1) * (b2 - a2 + c2 - b2 * x + e2 * x) - z * (c2 - a2 + e2 * x + f1 * x))
fz = z * (1 - z) * (c3 - b3 + d3 + c1 * x + b2 * y + e3 * x + f3 * y - c1 * x * y)

# 计算雅克比矩阵
yakebi = []
for f in [fx, fy, fz]:
    temp = []
    for i in [x, y, z]:
        fxx = sp.diff(f, i)  # 求导
        fxx = sp.simplify(fxx)  # 化简
        temp.append(fxx)
        print(temp)
    yakebi.append(temp)
yakebi_matrix = np.array(yakebi)  # 转为矩阵
print(yakebi_matrix)

# 计算特征值
eigenvals_dict = {}
for a in range(2):
    for b in range(2):
        for c in range(2):
            yk = []
            for yi in yakebi:
                yk.append([i.subs({x: a, y: b, z: c}) for i in yi])
            eigenvals_value = list(sp.Matrix(yk).eigenvals().keys())
            eigenvals_dict[f"{a}_{b}_{c}"] = eigenvals_value
for k, v in eigenvals_dict.items():
    print(k, v)