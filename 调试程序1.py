from scipy.stats import ttest_ind
import numpy as np

# 创建两组数据
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)

# 使用 ttest_ind 进行独立样本 t 检验
t_value, p_value = ttest_ind(data1, data2)

# 只显示 t 值
print("t 值:", t_value)