import random

mc = ['A', 'B', 'C', 'D', 'E']  # 定义一个含有五个元素的列表，用来存放这五个同学的名次顺序
while True:
    random.shuffle(mc)  # 对你刚才定义的列表元素进行随机排序，框里填你刚才定义的列表名
    if (mc[1] == 'D') + (mc[2] == 'B') == 1 and (mc[1] == 'C') + (mc[3] == 'E') == 1 and (mc[0] == 'E') + (
            mc[4] == 'A') == 1 and (mc[2] == 'C') + (mc[3] == 'A') == 1 and (mc[1] == 'B') + (
            mc[4] == 'D') == 1:  # 此处写判定条件，千万别忘了最后的冒号
        print(mc)  # 输出推断的名次顺序
        break
