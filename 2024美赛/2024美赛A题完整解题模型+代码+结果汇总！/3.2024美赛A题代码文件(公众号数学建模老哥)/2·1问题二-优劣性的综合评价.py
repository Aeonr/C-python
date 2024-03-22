import matplotlib.pyplot as plt
import numpy as np

def simulate_ecosystem(gender_ratio_variation):
    # 模拟七鳃鳗雄性比例的变化
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

        # 计算综合指标（加权求和）
        # 这里简单地加权求和，你可以根据实际情况调整权重
        composite_indicator[gen] = 0.4 * gender_ratio[gen] + 0.3 * predator_population[gen] + 0.2 * reproductive_success[gen] + 0.1 * food_resources[gen]

    return composite_indicator

def evaluate_population(gender_ratio_variation):
    # 模拟七鳃鳗种群
    composite_indicator = simulate_ecosystem(gender_ratio_variation)

    # 计算各个评价指标
    predation_control = np.mean(composite_indicator)  # 综合指标平均值表示对寄生虫的控制
    food_chain_role = np.max(composite_indicator)  # 综合指标最大值表示在食物链中的重要角色
    ecosystem_provider = np.sum(composite_indicator)  # 综合指标总和表示生态系统服务提供者
    adaptability = np.min(composite_indicator)  # 综合指标最小值表示环境适应性

    # 模拟其他劣势因素
    predation_threat = np.random.uniform(0.1, 0.5)  # 捕食其他物种的威胁程度
    reproduction_threat = np.random.uniform(0.1, 0.5)  # 繁殖受到威胁的程度
    overfishing_risk = np.random.uniform(0.1, 0.5)  # 过度捕捞的风险程度
    environmental_pressure = np.random.uniform(0.1, 0.5)  # 环境压力程度

    # 计算各个评价指标的权重
    weight_predation_control = 0.2
    weight_food_chain_role = 0.2
    weight_ecosystem_provider = 0.2
    weight_adaptability = 0.1
    weight_predation_threat = 0.1
    weight_reproduction_threat = 0.1
    weight_overfishing_risk = 0.1
    weight_environmental_pressure = 0.1

    # 计算综合评分
    overall_score = (weight_predation_control * predation_control +
                     weight_food_chain_role * food_chain_role +
                     weight_ecosystem_provider * ecosystem_provider +
                     weight_adaptability * adaptability -
                     weight_predation_threat * predation_threat -
                     weight_reproduction_threat * reproduction_threat -
                     weight_overfishing_risk * overfishing_risk -
                     weight_environmental_pressure * environmental_pressure)

    # 可视化结果
    labels = ['Predation Control', 'Food Chain Role', 'Ecosystem Provider', 'Adaptability',
              'Predation Threat', 'Reproduction Threat', 'Overfishing Risk', 'Environmental Pressure']
    values = [predation_control, food_chain_role, ecosystem_provider, adaptability,
              -predation_threat, -reproduction_threat, -overfishing_risk, -environmental_pressure]

    # 绘制直方图
    plt.figure(figsize=(12, 8))

    # 上半部分展示正面因素
    plt.subplot(2, 1, 1)
    plt.barh(labels[:4], values[:4], color=['green' if v >= 0 else 'red' for v in values[:4]])
    plt.title(f'Positive Aspects - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Score')

    # 在最大的两个指标上标注红线
    max_positive_indices = np.argpartition(values[:4], -2)[-2:]
    for idx in max_positive_indices:
        plt.axvline(x=values[idx], color='red', linestyle='--', label=f'Max {labels[idx]}')

    # 下半部分展示负面因素
    plt.subplot(2, 1, 2)
    plt.barh(labels[4:], values[4:], color=['green' if v >= 0 else 'red' for v in values[4:]])
    plt.title(f'Negative Aspects - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Score')


    max_negative_indices = np.argpartition(values[4:], -2)[-2:]
    for idx in max_negative_indices:
        plt.axvline(x=values[idx + 4], color='red', linestyle='--', label=f'Max {labels[idx + 4]}')

    plt.tight_layout()
    plt.show()

    # 输出对应的最大优势和劣势的标签
    max_positive_labels = [labels[idx] for idx in max_positive_indices]
    max_negative_labels = [labels[idx + 4] for idx in max_negative_indices]

    print(f'{gender_ratio_variation.capitalize()} Gender Ratio Variation:')
    print(f'Max Positive Aspects: {max_positive_labels}')
    print(f'Max Negative Aspects: {max_negative_labels}')

    return overall_score

# 模拟性别比例为1:1的情况
evaluate_population('equal')

# 模拟性别比例为70%雄性的情况
evaluate_population('male_dominant')

# 模拟性别比例为30%雄性的情况
evaluate_population('female_dominant')
