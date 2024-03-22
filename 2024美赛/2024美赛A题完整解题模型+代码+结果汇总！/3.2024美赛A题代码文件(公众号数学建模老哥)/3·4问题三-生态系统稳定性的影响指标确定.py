import matplotlib.pyplot as plt
import numpy as np

def highlight_max_confidence(ax, data, label):
    max_index = np.argmax(data)
    max_value = data[max_index]

    # Highlight the max value region in red
    ax.fill_between(range(len(data)), 0, max_value, where=(data == max_value), color='red', alpha=0.3, label='Max Value Region')

    # Annotate the max value
    ax.annotate(f'Max: {max_value:.2f}', xy=(max_index, max_value), xytext=(max_index, max_value + 0.1), arrowprops=dict(facecolor='black', shrink=0.05),)

    # Plot the data with confidence area
    ax.plot(range(len(data)), data, label=label)
    ax.fill_between(range(len(data)), data - 0.1, data + 0.1, color='gray', alpha=0.3, label='Confidence Area')

def simulate_ecosystem(gender_ratio_variation):
    if gender_ratio_variation == 'equal':
        initial_ratio = 0.5
    elif gender_ratio_variation == 'male_dominant':
        initial_ratio = 0.7
    elif gender_ratio_variation == 'female_dominant':
        initial_ratio = 0.3
    else:
        raise ValueError("Invalid gender ratio variation")

    generations = 50
    gender_ratio = np.zeros(generations)
    gender_ratio[0] = initial_ratio

    predator_population = np.ones(generations)
    reproductive_success = np.ones(generations)
    food_resources = np.ones(generations)
    parasite_population = np.ones(generations)
    other_predator_population = np.ones(generations)
    prey_population = np.ones(generations)
    fishery_yield = np.ones(generations)

    composite_indicator = np.zeros(generations)

    for gen in range(1, generations):
        gender_ratio[gen] = gender_ratio[gen - 1]

        reproductive_success[gen] = reproductive_success[gen - 1] - 0.005 * abs(gender_ratio[gen] - 0.5)

        predator_population[gen] = predator_population[gen - 1] * reproductive_success[gen]

        food_resources[gen] = food_resources[gen - 1] - 0.02

        parasite_population[gen] = parasite_population[gen - 1] + np.random.normal(0, 0.1)

        other_predator_population[gen] = other_predator_population[gen - 1] + 0.1 * predator_population[gen] - \
                                         0.05 * food_resources[gen]

        prey_population[gen] = prey_population[gen - 1] - 0.1 * other_predator_population[gen]

        fishery_yield[gen] = fishery_yield[gen - 1] + 0.15 * (1 - gender_ratio[gen]) * food_resources[gen]

        composite_indicator[gen] = 0.4 * gender_ratio[gen] + 0.3 * predator_population[gen] + \
                                   0.2 * reproductive_success[gen] + 0.1 * food_resources[gen]

    return composite_indicator, parasite_population, other_predator_population, prey_population, fishery_yield

def evaluate_population(gender_ratio_variation):
    composite_indicator, parasite_population, other_predator_population, prey_population, fishery_yield = simulate_ecosystem(gender_ratio_variation)

    # Visualize results
    generations = np.arange(50)

    plt.figure(figsize=(12, 16))

    # Plot composite indicator dynamics
    plt.subplot(6, 1, 1)
    highlight_max_confidence(plt, composite_indicator, 'Composite Indicator')
    plt.title(f'Composite Indicator Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Composite Indicator')
    plt.legend()

    # Plot parasite population dynamics
    plt.subplot(6, 1, 2)
    highlight_max_confidence(plt, parasite_population, 'Parasite Population')
    plt.title(f'Parasite Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Parasite Population')
    plt.legend()

    # Plot other predator population dynamics
    plt.subplot(6, 1, 3)
    highlight_max_confidence(plt, other_predator_population, 'Other Predator Population')
    plt.title(f'Other Predator Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Other Predator Population')
    plt.legend()

    # Plot prey population dynamics
    plt.subplot(6, 1, 4)
    highlight_max_confidence(plt, prey_population, 'Prey Population')
    plt.title(f'Prey Population Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Prey Population')
    plt.legend()

    # Plot fishery yield dynamics
    plt.subplot(6, 1, 5)
    highlight_max_confidence(plt, fishery_yield, 'Fishery Yield')
    plt.title(f'Fishery Yield Dynamics - {gender_ratio_variation.capitalize()} Gender Ratio Variation')
    plt.xlabel('Generations')
    plt.ylabel('Fishery Yield')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Simulate equal gender ratio scenario
evaluate_population('equal')

# Simulate male-dominant gender ratio scenario
evaluate_population('male_dominant')

# Simulate female-dominant gender ratio scenario
evaluate_population('female_dominant')
