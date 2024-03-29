import matplotlib.pyplot as plt
import numpy as np

def simulate_gender_ratio_effect(initial_gender_ratio, food_supply_factor):
    generations = 50
    gender_ratio = np.linspace(initial_gender_ratio, 1 - initial_gender_ratio, generations)
    print(gender_ratio)
    food_supply = food_supply_factor / gender_ratio  # 简化的关系，实际可根据情况调整

    return gender_ratio, food_supply

# 模拟性别比例从全雌性到全雄性的变化
initial_ratios = [0.1, 0.3, 0.5, 0.7, 0.9]
food_factor = 100  # 初始食物资源数量

plt.figure(figsize=(10, 6))

plt.xlim(0, 1)  # x轴范围
# plt.ylim(0, 100)   # y轴范围

gender_ratio, food_supply = simulate_gender_ratio_effect(initial_ratios[0], food_factor)
print(gender_ratio, food_supply)
plt.plot(gender_ratio, food_supply, label=f'Initial Gender Ratio: 0.1')

gender_ratio, food_supply = simulate_gender_ratio_effect(initial_ratios[1], food_factor)
print(gender_ratio, food_supply)
plt.plot(gender_ratio, food_supply, label=f'Initial Gender Ratio: 0.1')

gender_ratio, food_supply = simulate_gender_ratio_effect(initial_ratios[2], food_factor)
print(gender_ratio, food_supply)
plt.plot(gender_ratio, food_supply, label=f'Initial Gender Ratio: 0.1')

gender_ratio, food_supply = simulate_gender_ratio_effect(initial_ratios[3], food_factor)
print(gender_ratio, food_supply)
plt.plot(gender_ratio, food_supply, label=f'Initial Gender Ratio: 0.1')

plt.title('Effect of Gender Ratio on Food Supply')
plt.xlabel('Gender Ratio')
plt.ylabel('Food Supply')
plt.legend()
plt.grid(True)
plt.show()
