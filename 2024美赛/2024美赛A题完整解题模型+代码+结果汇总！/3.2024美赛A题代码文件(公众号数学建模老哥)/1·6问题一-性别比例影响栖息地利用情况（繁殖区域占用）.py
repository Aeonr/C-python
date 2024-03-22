import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
num_generations = 100  # 模拟的世代数
initial_female_ratio = 0.5  # 初始雌性比例
initial_resource_area_ratio = 0.7  # 初始资源区占用比例
habitat_capacity = 1.0  # 栖息地总面积

# 模拟函数
def simulate_population(num_generations, initial_female_ratio, initial_resource_area_ratio, habitat_capacity):
    female_ratio = initial_female_ratio
    resource_area_ratio = initial_resource_area_ratio
    habitat_occupation = []

    for generation in range(num_generations):
        # 计算每一代的栖息地占用情况
        occupation = habitat_capacity * female_ratio * resource_area_ratio
        habitat_occupation.append(occupation)

        # 根据当前性别比例和资源区占用比例更新下一代性别比例和资源区占用比例
        # 增加随机性的程度，使结果更加波动
        female_ratio += np.random.uniform(-0.1, 0.1)
        female_ratio = np.clip(female_ratio, 0, 1)  # 保持在合理范围内

        resource_area_ratio += np.random.uniform(-0.2, 0.2)
        resource_area_ratio = np.clip(resource_area_ratio, 0, 1)  # 保持在合理范围内

    return habitat_occupation

# 运行模拟
habitat_occupation = simulate_population(num_generations, initial_female_ratio, initial_resource_area_ratio, habitat_capacity)

# 绘制模拟结果
generations = range(num_generations)
plt.plot(generations, habitat_occupation, label='Habitat Occupation')
plt.axhline(habitat_capacity, color='red', linestyle='--', label='Max Habitat Capacity')
plt.title('Seven-Gill Shark Population Simulation with Resource Area (More Fluctuation)')
plt.xlabel('Generations')
plt.ylabel('Habitat Occupation')
plt.legend()
plt.show()
