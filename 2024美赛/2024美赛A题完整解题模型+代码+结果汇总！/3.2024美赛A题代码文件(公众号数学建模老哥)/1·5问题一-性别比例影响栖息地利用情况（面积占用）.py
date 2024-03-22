import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
num_generations = 100  # 模拟的世代数
initial_female_ratio = 0.5  # 初始雌性比例
habitat_capacity = 1.0  # 栖息地总面积

# 模拟函数
def simulate_population(num_generations, initial_female_ratio, habitat_capacity):
    female_ratio = initial_female_ratio
    habitat_occupation = []

    for generation in range(num_generations):
        # 模拟性别比例变化
        male_ratio = 1 - female_ratio

        # 模拟栖息地占用情况变化
        occupation = habitat_capacity * female_ratio
        habitat_occupation.append(occupation)

        # 根据当前性别比例更新下一代性别比例（这里简单地使用随机变化）
        female_ratio += np.random.uniform(-0.1, 0.1)
        female_ratio = np.clip(female_ratio, 0, 1)  # 保持在合理范围内

    return habitat_occupation

# 运行模拟
habitat_occupation = simulate_population(num_generations, initial_female_ratio, habitat_capacity)

# 绘制模拟结果
generations = range(num_generations)
plt.plot(generations, habitat_occupation, label='Habitat Occupation')
plt.axhline(habitat_capacity, color='red', linestyle='--', label='Max Habitat Capacity')
plt.title('Seven-Gill Shark Population Simulation')
plt.xlabel('Generations')
plt.ylabel('Habitat Occupation')
plt.legend()
plt.show()
