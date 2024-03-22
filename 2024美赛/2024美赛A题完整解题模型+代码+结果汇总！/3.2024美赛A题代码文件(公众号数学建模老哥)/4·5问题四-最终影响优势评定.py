import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 假设有四个评价指标，分别是性别比例的变化（自变量）、竞争关系的复杂性、寄生虫种群的变化和食物网的复杂性（因变量）
indicators = {
    'GenderRatioChange': [0.2, 0.4, 0.6, 0.8, 1.0],  # 假设性别比例变化的情况，值越大表示变化越大
    'CompetitionComplexity': [0.3, 0.5, 0.7, 0.9, 1.0],  # 假设竞争关系的复杂性，值越大表示复杂性越高
    'ParasitePopulationChange': [0.1, 0.3, 0.5, 0.7, 1.0],  # 假设寄生虫种群变化，值越大表示变化越大
    'FoodWebComplexity': [0.2, 0.4, 0.6, 0.8, 1.0]  # 假设食物网的复杂性，值越大表示复杂性越高
}

# 创建一个DataFrame来存储指标数据
df = pd.DataFrame(indicators)

# 设定权重阈值
weight_threshold = 0.6

# 判断是否所有因素的权重都超过阈值
advantageous_scenarios = df[(df['CompetitionComplexity'] > weight_threshold) &
                             (df['ParasitePopulationChange'] > weight_threshold) &
                             (df['FoodWebComplexity'] > weight_threshold)]

# 输出结果
print("Scenarios where all weights are advantageous:")
print(advantageous_scenarios)

# 可视化指标
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle('Evaluation of Scenarios')

# Plot Gender Ratio Change
axes[0, 0].plot(df['GenderRatioChange'], marker='o', linestyle='-', color='blue')
axes[0, 0].axhline(y=weight_threshold, color='red', linestyle='--', label='Threshold')
axes[0, 0].set_title('Gender Ratio Change')
axes[0, 0].set_xlabel('Scenario')
axes[0, 0].set_ylabel('Value')
axes[0, 0].legend()

# Plot Competition Complexity
axes[0, 1].plot(df['CompetitionComplexity'], marker='o', linestyle='-', color='green')
axes[0, 1].axhline(y=weight_threshold, color='red', linestyle='--', label='Threshold')
axes[0, 1].set_title('Competition Complexity')
axes[0, 1].set_xlabel('Scenario')
axes[0, 1].set_ylabel('Value')
axes[0, 1].legend()

# Plot Parasite Population Change
axes[1, 0].plot(df['ParasitePopulationChange'], marker='o', linestyle='-', color='orange')
axes[1, 0].axhline(y=weight_threshold, color='red', linestyle='--', label='Threshold')
axes[1, 0].set_title('Parasite Population Change')
axes[1, 0].set_xlabel('Scenario')
axes[1, 0].set_ylabel('Value')
axes[1, 0].legend()

# Plot Food Web Complexity
axes[1, 1].plot(df['FoodWebComplexity'], marker='o', linestyle='-', color='purple')
axes[1, 1].axhline(y=weight_threshold, color='red', linestyle='--', label='Threshold')
axes[1, 1].set_title('Food Web Complexity')
axes[1, 1].set_xlabel('Scenario')
axes[1, 1].set_ylabel('Value')
axes[1, 1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
