import matplotlib.pyplot as plt
import numpy as np

def simulate_ecosystem(food_availability):
    # 模拟七鳃鳗雄性比例的变化
    if food_availability == 'low':
        initial_ratio = 0.22  # 假设初始雄性比例为 22%
    elif food_availability == 'high':
        initial_ratio = 0.56  # 假设初始雄性比例为 56%
    else:
        raise ValueError("Invalid food availability")

    generations = 50
    gender_ratio = np.zeros(generations)
    gender_ratio[0] = initial_ratio

    predator_population = np.ones(generations)  # 初始捕食者数量为 1

    for gen in range(1, generations):
        # 模拟雄性比例的变化，根据食物可得性调整
        if food_availability == 'low':
            gender_ratio[gen] = gender_ratio[gen - 1] + 0.01  # 在食物较少的环境中，雄性比例增加
            predator_population[gen] = predator_population[gen - 1] * (1 + 0.02)  # 捕食者数量增加
        elif food_availability == 'high':
            gender_ratio[gen] = gender_ratio[gen - 1] - 0.01  # 在食物较多的环境中，雄性比例减少
            predator_population[gen] = predator_population[gen - 1] * (1 - 0.01)  # 捕食者数量减少

    return gender_ratio, predator_population

# 模拟食物可得性较低的情况
low_food_gender_ratio, low_food_predator_population = simulate_ecosystem('low')

# 模拟食物可得性较高的情况
high_food_gender_ratio, high_food_predator_population = simulate_ecosystem('high')

# 绘制结果
generations = np.arange(50)
plt.figure(figsize=(10, 5))

# 七鳃鳗性别比例图
plt.subplot(1, 2, 1)
plt.plot(generations, low_food_gender_ratio, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_gender_ratio, label='High Food Availability', linewidth=2)
plt.title('Simulated Gender Ratio in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Gender Ratio')
plt.legend()

# 捕食者数量图
plt.subplot(1, 2, 2)
plt.plot(generations, low_food_predator_population, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_predator_population, label='High Food Availability', linewidth=2)
plt.title('Simulated Predator Population in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Predator Population')
plt.legend()

plt.tight_layout()
plt.show()
