# 导入需要的库  
import networkx as nx
import matplotlib.pyplot as plt

# 创建一个复杂的食物网边的集合  
food_web_edges = {
    'Seven-gilled eel': ['Big fish', 'Small insect'],  # 七鳃鳗捕食大鱼和小昆虫  
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

# 绘制图  
pos = nx.spring_layout(food_web_graph)  # 使用弹簧布局算法确定节点位置
labels = {node: node for node in food_web_graph.nodes()}  # 定义节点标签，这里直接使用节点名作为标签

# 高亮显示“Seven-gilled eel”节点  
node_colors = ['red' if node == 'Seven-gilled eel' else 'skyblue' for node in
               food_web_graph.nodes()]  # 红色表示七鳃鳗，其他为天蓝色
node_sizes = [1200 if node == 'Seven-gilled eel' else 800 for node in food_web_graph.nodes()]  # 七鳃鳗的节点大小为1200，其他为800

nx.draw(food_web_graph, pos, with_labels=True, labels=labels, node_size=node_sizes, node_color=node_colors, font_size=8,
        font_color='black', font_weight='bold', edge_color='gray', linewidths=1,
        arrowsize=10)  # 使用networkx的draw函数绘制图，设置各种参数
plt.title("Food Web")  # 设置图的标题为“食物网”
plt.show()  # 显示图