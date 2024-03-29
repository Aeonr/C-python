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
    reproductive_success = np.ones(generations)  # 初始繁殖成功率为 1

    for gen in range(1, generations):
        # 模拟雄性比例的变化，根据食物可得性调整
        if food_availability == 'low':
            gender_ratio[gen] = gender_ratio[gen - 1] + 0.01  # 在食物较少的环境中，雄性比例增加
        elif food_availability == 'high':
            gender_ratio[gen] = gender_ratio[gen - 1] - 0.01  # 在食物较多的环境中，雄性比例减少

        # 模拟繁殖成功率的变化，根据性别比例调整
        reproductive_success[gen] = reproductive_success[gen - 1] - 0.005 * abs(gender_ratio[gen] - 0.5)

        # 根据捕食者数量和繁殖成功率更新下一代捕食者数量
        predator_population[gen] = predator_population[gen - 1] * reproductive_success[gen]

    # 模拟食物资源的变化
    food_resources = np.ones(generations)  # 初始食物资源为 1

    for gen in range(1, generations):
        # 在食物资源下降的环境中，减少食物资源
        if food_availability == 'low':
            food_resources[gen] = food_resources[gen - 1] - 0.02
        elif food_availability == 'high':
            # 在食物资源增加的环境中，增加食物资源
            food_resources[gen] = food_resources[gen - 1] + 0.02

    return gender_ratio, predator_population, reproductive_success, food_resources

# 模拟食物可得性较低的情况
low_food_gender_ratio, low_food_predator_population, low_food_reproductive_success, low_food_resources = simulate_ecosystem('low')

# 模拟食物可得性较高的情况
high_food_gender_ratio, high_food_predator_population, high_food_reproductive_success, high_food_resources = simulate_ecosystem('high')

# 绘制结果
generations = np.arange(50)
plt.figure(figsize=(15, 10))

# 七鳃鳗性别比例图
plt.subplot(2, 2, 1)
plt.plot(generations, low_food_gender_ratio, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_gender_ratio, label='High Food Availability', linewidth=2)
plt.title('Simulated Gender Ratio in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Gender Ratio')
plt.legend()

# 捕食者数量图
plt.subplot(2, 2, 2)
plt.plot(generations, low_food_predator_population, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_predator_population, label='High Food Availability', linewidth=2)
plt.title('Simulated Predator Population in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Predator Population')
plt.legend()

# 繁殖成功率图
plt.subplot(2, 2, 3)
plt.plot(generations, low_food_reproductive_success, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_reproductive_success, label='High Food Availability', linewidth=2)
plt.title('Simulated Reproductive Success in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Reproductive Success')
plt.legend()

# 食物资源变化图
plt.subplot(2, 2, 4)
plt.plot(generations, low_food_resources, label='Low Food Availability', linewidth=2)
plt.plot(generations, high_food_resources, label='High Food Availability', linewidth=2)
plt.title('Simulated Food Resources in Response to Food Availability')
plt.xlabel('Generations')
plt.ylabel('Food Resources')
plt.legend()

plt.tight_layout()
plt.show()
