import matplotlib.pyplot as plt
import numpy as np

def simulate_ecosystem(gender_ratio_variation):
    # 模拟七鳃鳗雄性比例的变化
    if gender_ratio_variation == 'equal':
        initial_ratio = 0.5  # 初始雄性比例为 50%
    elif gender_ratio_variation == 'male_dominant':
        initial_ratio = 0.9  # 初始雄性比例为 90%
    elif gender_ratio_variation == 'female_dominant':
        initial_ratio = 0.1  # 初始雄性比例为 10%
    else:
        raise ValueError("Invalid gender ratio variation")

    generations = 50
    gender_ratio = np.zeros(generations)
    gender_ratio[0] = initial_ratio

    predator_population = np.ones(generations)  # 初始捕食者数量为 1
    reproductive_success = np.ones(generations)  # 初始繁殖成功率为 1
    food_resources = np.ones(generations)  # 初始食物资源为 1

    composite_indicator = np.zeros(generations)  # 初始综合指标为 0

    for gen in range(1, generations):
        # 模拟雄性比例的变化
        gender_ratio[gen] = gender_ratio[gen - 1]

        # 模拟繁殖成功率的变化，根据性别比例调整
        reproductive_success[gen] = reproductive_success[gen - 1] - 0.005 * abs(gender_ratio[gen] - 0.5)

        # 根据捕食者数量和繁殖成功率更新下一代捕食者数量
        predator_population[gen] = predator_population[gen - 1] * reproductive_success[gen]

        # 模拟食物资源的变化
        food_resources[gen] = food_resources[gen - 1] - 0.02

        # 计算综合指标（加权求和），增加对雌性的权重
        # 这里简单地加权求和，你可以根据实际情况调整权重
        composite_indicator[gen] = 0.3 * gender_ratio[gen] + 0.4 * predator_population[gen] + 0.2 * reproductive_success[gen] + 0.1 * food_resources[gen]

    # 使用正态分布生成平滑曲线
    composite_indicator_smooth = np.convolve(composite_indicator, np.ones(5)/5, mode='valid')

    return composite_indicator_smooth

# 模拟性别比例为1:1的情况
equal_gender_ratio_indicator = simulate_ecosystem('equal')

# 模拟性别比例为90%雄性的情况
male_dominant_indicator = simulate_ecosystem('male_dominant')

# 模拟性别比例为10%雄性的情况
female_dominant_indicator = simulate_ecosystem('female_dominant')

# 绘制结果
generations = np.arange(len(equal_gender_ratio_indicator))
plt.figure(figsize=(10, 5))

# 综合指标图
plt.plot(generations, equal_gender_ratio_indicator, label='Equal Gender Ratio', linewidth=2)
plt.plot(generations, male_dominant_indicator, label='Male Dominant', linewidth=2)
plt.plot(generations, female_dominant_indicator, label='Female Dominant', linewidth=2)
plt.title('Smooth Composite Indicator in Different Gender Ratios')
plt.xlabel('Generations')
plt.ylabel('Composite Indicator')
plt.legend()
plt.show()
