import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 模拟七鳃鳗性别比例变化对生态系统的影响

# 参数设置
num_generations = 100
initial_population = 1000
male_ratio = 0.5  # 初始性别比例

# 初始化种群和生态系统稳定性
population = np.zeros((num_generations, 2))  # 列0表示雌性，列1表示雄性
ecosystem_stability = np.zeros(num_generations)

population[0] = [initial_population * (1 - male_ratio), initial_population * male_ratio]

# 模拟种群和生态系统变化
for generation in range(1, num_generations):
    # 这里可以添加更复杂的模型，考虑繁殖、食物链等因素
    # 这里简化为性别比例随机变化，同时引入生态系统稳定性因素
    male_ratio += np.random.uniform(-0.05, 0.05)  # 随机变化性别比例
    male_ratio = np.clip(male_ratio, 0.1, 0.9)  # 限制性别比例在0.1到0.9之间
    population[generation] = [initial_population * (1 - male_ratio), initial_population * male_ratio]

    # 模拟生态系统稳定性的变化，这里简化为基于性别比例的影响
    ecosystem_stability[generation] = 1 - abs(male_ratio - 0.5)  # 假设性别比例越接近均衡，生态系统越稳定

# 可视化结果
sns.set(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制雌性种群和雄性种群的曲线
color = 'tab:red'
ax1.set_xlabel('Generations')
ax1.set_ylabel('Population Size', color=color)
ax1.plot(population[:, 0], label='Female Population', linewidth=2, color=color)
ax1.plot(population[:, 1], label='Male Population', linewidth=2, linestyle='dashed', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 创建第二个y轴用于绘制生态系统稳定性
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Ecosystem Stability', color=color)
ax2.plot(ecosystem_stability, label='Ecosystem Stability', linewidth=2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# 设置图表标题
plt.title('Population Dynamics and Ecosystem Stability of Seven-Gilled Shark')

# 添加图例
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# 显示图表
plt.show()
