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

# 提取第一个自变量和后三个因变量
target_variable = df['GenderRatioChange']
dependent_variables = df[['CompetitionComplexity', 'ParasitePopulationChange', 'FoodWebComplexity']]

# 标准化指标数据
normalized_target_variable = target_variable / np.sqrt((target_variable ** 2).sum())
normalized_dependent_variables = dependent_variables / np.sqrt((dependent_variables ** 2).sum())

# 计算正理想解和负理想解
ideal_positive = normalized_dependent_variables.max()
ideal_negative = normalized_dependent_variables.min()

# 计算正理想解和负理想解之间的距离
distance_positive = np.sqrt(((normalized_dependent_variables - ideal_positive) ** 2).sum(axis=1))
distance_negative = np.sqrt(((normalized_dependent_variables - ideal_negative) ** 2).sum(axis=1))

# 计算综合得分
scores = distance_negative / (distance_positive + distance_negative)

# 将得分添加到DataFrame中
df['Score'] = scores

# 根据得分进行排名
df['Rank'] = df['Score'].rank(ascending=False)

# 输出结果
print(df)

# 可视化得分
plt.bar(df.index, df['Score'])
plt.xlabel('Scenario')
plt.ylabel('TOPSIS Score')
plt.title('TOPSIS Evaluation of Scenarios')
plt.xticks(df.index, df['Rank'].astype(int), rotation=45)

# 找到得分最高的情景并标记
max_score_index = df['Score'].idxmax()
plt.annotate(f"Best Scenario (#{max_score_index + 1})",
             xy=(max_score_index, df['Score'][max_score_index]),
             xytext=(max_score_index + 0.5, df['Score'][max_score_index] + 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
