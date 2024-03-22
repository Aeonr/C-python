import numpy as np
import matplotlib.pyplot as plt


class EelAgent:
    def __init__(self, gender, growth_rate):
        self.gender = gender
        self.growth_rate = growth_rate

    def reproduce(self, gender_ratio):
        # 模拟繁殖，受性别比例的影响
        reproduction_success_rate = gender_ratio  # 假设繁殖成功率与性别比例成正比
        reproduction_success = np.random.rand() < reproduction_success_rate
        return reproduction_success


class Ecosystem:
    def __init__(self, initial_gender_ratio, initial_resource_availability):
        self.agents = []
        self.gender_ratio = initial_gender_ratio
        self.resource_availability = initial_resource_availability
        self.reproduction_success_history = []

    def update_gender_ratio(self):
        # 模拟资源影响性别比例
        self.gender_ratio = min(1, self.resource_availability)

    def simulate(self, num_steps):
        for _ in range(num_steps):
            self.update_gender_ratio()

            reproduction_success_rates = []

            for agent in self.agents:
                reproduction_success = agent.reproduce(self.gender_ratio)
                reproduction_success_rates.append(reproduction_success)

            # 记录平均繁殖成功率
            average_reproduction_success_rate = np.mean(reproduction_success_rates)
            self.reproduction_success_history.append(average_reproduction_success_rate)


if __name__ == "__main__":
    initial_gender_ratio = 0.5
    initial_resource_availability = 0.8

    ecosystem = Ecosystem(initial_gender_ratio, initial_resource_availability)

    # 创建一些七鳃鳗代理
    num_agents = 100
    for _ in range(num_agents):
        gender = np.random.choice(["male", "female"])
        growth_rate = np.random.uniform(0.1, 0.5)
        agent = EelAgent(gender, growth_rate)
        ecosystem.agents.append(agent)

    # 模拟100个时间步
    ecosystem.simulate(100)

    # 可视化
    plt.figure(figsize=(10, 6))
    plt.plot(ecosystem.reproduction_success_history, label='Reproduction Success Rate')

    # 找到最高繁殖率的位置
    max_reproduction_rate_index = np.argmax(ecosystem.reproduction_success_history)


    plt.axhline(y=ecosystem.reproduction_success_history[max_reproduction_rate_index], color='red', linestyle='--',
                label='Max Reproduction Rate')

    plt.xlabel('Time Steps')
    plt.ylabel('Reproduction Success Rate')
    plt.legend()
    plt.show()
