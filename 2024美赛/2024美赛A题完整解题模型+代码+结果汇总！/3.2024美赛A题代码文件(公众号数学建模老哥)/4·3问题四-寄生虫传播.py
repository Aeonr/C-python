# 导入需要的库  
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 创建一个复杂的食物网边的集合
food_web_edges = {
    'Seven-gilled eel (Male)': ['Big fish', 'Small insect'],  # 七鳃鳗（雄性）捕食大鱼和小昆虫
    'Seven-gilled eel (Female)': ['Big fish', 'Small insect'],  # 七鳃鳗（雌性）捕食大鱼和小昆虫
    'Big fish': ['Small fish', 'Crustaceans'],  # 大鱼捕食小鱼和甲壳动物
    'Small fish': ['Plankton'],  # 小鱼捕食浮游生物
    'Crustaceans': ['Small insect', 'Crabs'],  # 甲壳动物捕食小昆虫和螃蟹
    'Crabs': ['Small insect'],  # 螃蟹捕食小昆虫
    'Small insect': ['Plankton'],  # 小昆虫捕食浮游生物
    'Plankton': ['Plants'],  # 浮游生物捕食植物
    # 添加其他生物及其捕食关系...
}

# 创建一个有向图
food_web_graph = nx.DiGraph()

# 添加节点和边
for predator, prey_list in food_web_edges.items():
    food_web_graph.add_node(predator)  # 添加捕食者节点
    food_web_graph.add_edges_from((predator, prey) for prey in prey_list)  # 添加捕食关系边

# 模拟寄生虫种群随时间的变化
time_steps = 10  # 时间步数
parasite_population = np.zeros((time_steps,))  # 初始化寄生虫种群数组

# 为雄性和雌性的七鳃鳗分配不同的寄生虫负载量
parasite_loads = {'Seven-gilled eel (Male)': 5, 'Seven-gilled eel (Female)': 3}  # 寄生虫负载量字典

# 性别比例随时间变化
gender_ratio = np.linspace(0, 1, time_steps)  # 生成时间步数对应的性别比例数组

for i, ratio in enumerate(gender_ratio):
    male_count = int(ratio * len(food_web_edges))  # 计算当前时间步的雄性数量
    female_count = len(food_web_edges) - male_count  # 计算当前时间步的雌性数量

    total_parasite_count = male_count * parasite_loads['Seven-gilled eel (Male)'] + female_count * parasite_loads[
        'Seven-gilled eel (Female)']  # 计算总寄生虫数量
    parasite_population[i] = total_parasite_count  # 将总寄生虫数量存入数组中

# 绘制线形图
plt.plot(gender_ratio, parasite_population, marker='o', linestyle='-')  # 绘制线形图，标记为圆圈，线型为实线
plt.xlabel('Gender Ratio (Male/Female)')  # X轴标签为“性别比例（雄/雌）”
plt.ylabel('Total Parasite Population')  # Y轴标签为“总寄生虫种群”
plt.title('Impact of Gender Ratio on Parasite Population')  # 图标题为“性别比例对寄生虫种群的影响”
plt.grid(True)  # 显示网格线
plt.show()  # 显示图形