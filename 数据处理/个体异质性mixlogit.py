import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(42)

# 定义样本数量和属性
n_individuals = 10000  # 样本量
n_choices = 8  # 每个个体的选择集数量

# 属性取值范围
price = np.random.randint(20000, 40000, n_choices)
range_km = np.random.randint(150, 400, n_choices)
charging_time = np.random.randint(30, 120, n_choices)

# 每个个体生成选择数据
data = []

for i in range(n_individuals):
    # 随机生成个体偏好
    beta_price = np.random.normal(-0.01, 0.005)
    beta_range = np.random.normal(0.02, 0.01)
    beta_charging_time = np.random.normal(-0.05, 0.02)

    # 计算每个选择的效用
    utility = (beta_price * price + beta_range * range_km + beta_charging_time * charging_time)

    # 根据效用生成选择
    choice = np.argmax(utility)

    for j in range(n_choices):
        data.append([i, price[j], range_km[j], charging_time[j], 1 if j == choice else 0])

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['individual', 'price', 'range_km', 'charging_time', 'choice'])
print(df.head())

# 定义效用模型
# 特征缩放
df['price_scaled'] = df['price'] / 1000
df['range_scaled'] = df['range_km'] / 100
df['charging_time_scaled'] = df['charging_time'] / 10

X = df[['price_scaled', 'range_scaled', 'charging_time_scaled']]
y = df['choice']

# 添加截距项
X = sm.add_constant(X)

# 使用Logit模型进行初步估计
logit_model = sm.Logit(y, X)
result = logit_model.fit()
print(result.summary())

# 获取初始参数估计
initial_params = result.params.values

# 模拟顺序设计，更新选择集并估计WTP
individual_WTPs = []

for i in range(n_individuals):
    # 使用估计的参数生成个体特定的效用参数
    beta_price = np.random.normal(initial_params[1], 0.005)
    beta_range = np.random.normal(initial_params[2], 0.01)
    beta_charging_time = np.random.normal(initial_params[3], 0.02)

    # 计算WTP
    WTP_range = -beta_range / beta_price
    individual_WTPs.append(WTP_range)

# 将个体的WTP结果转换为DataFrame
df_wtp = pd.DataFrame({
    'individual': np.arange(n_individuals),
    'WTP_range': individual_WTPs
})
print(df_wtp.head())

# 可视化个体WTP分布
plt.hist(df_wtp['WTP_range'], bins=20, edgecolor='black')
plt.xlabel('WTP for Range (per km)')
plt.ylabel('Frequency')
plt.title('Distribution of Individual WTP for Range')
plt.show()
