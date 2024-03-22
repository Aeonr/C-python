import matplotlib.pyplot as plt
import numpy as np

def simulate_ecosystem(gender_ratio_variation):
    if gender_ratio_variation == 'equal':
        initial_ratio = 0.5  # 初始雄性比例为 50%
    elif gender_ratio_variation == 'male_dominant':
        initial_ratio = 0.7  # 初始雄性比例为 70%
    elif gender_ratio_variation == 'female_dominant':
        initial_ratio = 0.3  # 初始雄性比例为 30%
    else:
        raise ValueError("Invalid gender ratio variation")

    generations = 50
    gender_ratio = np.zeros(generations)
    gender_ratio[0] = initial_ratio

    predator_population = np.ones(generations)  # 初始捕食者数量为 1
    reproductive_success = np.ones(generations)  # 初始繁殖成功率为 1
    food_resources = np.ones(generations)  # 初始食物资源为 1
    parasite_population = np.ones(generations)  # 初始寄生虫数量为 1
    other_predator_population = np.ones(generations)  # 初始其他捕食者数量为 1
    prey_population = np.ones(generations)  # 初始被捕食者数量为 1

    composite_indicator = np.zeros(generations)  # 初始综合指标为 0

    for gen in range(1, generations):
        gender_ratio[gen] = gender_ratio[gen - 1]

        # 模拟繁殖成功率的变化，根据性别比例调整
        reproductive_success[gen] = reproductive_success[gen - 1] - 0.005 * abs(gender_ratio[gen] - 0.5)

        # 根据捕食者数量和繁殖成功率更新下一代捕食者数量
        predator_population[gen] = predator_population[gen - 1] * reproductive_success[gen]

        # 模拟食物资源的变化
        food_resources[gen] = food_resources[gen - 1] - 0.02

        # 引入一些波动，模拟寄生虫数量的变化
        parasite_population[gen] = parasite_population[gen - 1] + np.random.normal(0, 0.1)

        # 模拟其他捕食者数量的变化，根据七鳃鳗数量和食物资源调整
        other_predator_population[gen] = other_predator_population[gen - 1] + 0.1 * predator_population[gen] - \
                                         0.05 * food_resources[gen]

        # 模拟被捕食者数量的变化，根据其他捕食者数量调整
        prey_population[gen] = prey_population[gen - 1] - 0.1 * other_predator_population[gen]

        # 计算综合指标
        composite_indicator[gen] = 0.4 * gender_ratio[gen] + 0.3 * predator_population[gen] + \
                                   0.2 * reproductive_success[gen] + 0.1 * food_resources[gen]

    return composite_indicator, parasite_population, other_predator_population, prey_population

def evaluate_population(gender_ratio_variation):
    composite_indicator, parasite_population, other_predator_population, prey_population = simulate_ecosystem(gender_ratio_variation)

    # 可视化结果
    generations = np.arange(50)

    plt.figure(figsize=(12, 12))

    # 绘制综合指标变化图
    plt.subplot(4, 1, 1)
    plt.plot(generations, composite_indicator, label='Composite Indicator')
    plt.title(f'Composite Indicator Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Composite Indicator')
    plt.legend()

    # 绘制寄生虫数量变化图
    plt.subplot(4, 1, 2)
    plt.plot(generations, parasite_population, label='Parasite Population')
    plt.title(f'Parasite Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Parasite Population')
    plt.legend()

    # 绘制其他捕食者数量变化图
    plt.subplot(4, 1, 3)
    plt.plot(generations, other_predator_population, label='Other Predator Population')
    plt.title(f'Other Predator Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Other Predator Population')
    plt.legend()

    # 绘制被捕食者数量变化图
    plt.subplot(4, 1, 4)
    plt.plot(generations, prey_population, label='Prey Population')
    plt.title(f'Prey Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Prey Population')
    plt.legend()

    plt.tight_layout()
    plt.show()

# 模拟性别比例为1:1的情况
evaluate_population('equal')

# 模拟性别比例为70%雄性的情况
evaluate_population('male_dominant')

# 模拟性别比例为30%雄性的情况
evaluate_population('female_dominant')
