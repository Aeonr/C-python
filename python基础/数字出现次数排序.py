n_cnt = int(input())
line = input()
n_str_list = line.split()
n_list = []
for n_str in n_str_list:
    n = int(n_str)
    n_list.append(n)

dict_n_cnt = {}
for n in n_list:
    if n in dict_n_cnt:
        dict_n_cnt[n] += 1
    else:
        dict_n_cnt[n] = 1

def cmp(item1, item2):
    if item1[1] == item2[1]:  # 出现次数一样，则按数字从小到大排序
        if item1[0] < item2[0]:
            return -1;
        elif item1[0] > item2[0]:
            return 1
    else:
        if item1[1] < item2[1]:  # 按出现次数从大到小排序
            return 1;
        elif item1[1] > item2[1]:
            return -1

import functools
list_n_cnt = list(dict_n_cnt.items())
list_n_cnt.sort(key=functools.cmp_to_key(cmp))

for item in list_n_cnt:
    print(item[0], item[1])
