import pandas as pd
import numpy as np

# 数据读取
data1 = pd.read_excel("C:\\Users\\CYH10\\Desktop\\线上问卷原始版.xlsx", sheet_name='牛奶')
data2 = pd.read_stata("C:\\Users\\CYH10\\Desktop\\选项卡片.dta")
# 数据转置
data_melt = pd.melt(data1, id_vars=['id'], value_vars=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'], var_name='variable', value_name='value')
# 数据排序
data_sort = data_melt.sort_values(['id', 'variable'])
# 数据重复
data_repeat = pd.DataFrame(np.repeat(data_sort, 4, axis=0))
data_repeat = data_repeat.rename(columns={0: 'id', 1: 'set', 2: 'choice'})
# 序列生成
sequence = np.array([1, 2, 3, 4])
data_repeat['choice_card'] = np.tile(sequence, 8780)
data_repeat['set'] = data_repeat['set'].str[1:]
# 真实选择判断
data_repeat['choice'] = np.where(data_repeat['choice'] == data_repeat['choice_card'], 1, 0)
# 数据类型转换
data_repeat['set'] = data_repeat['set'].astype('int')
data_repeat['choice_card'] = data_repeat['choice_card'].astype('int')
data2['set'] = data2['set'].astype('int')
data2['choice_card'] = data2['choice_card'].astype('int')
# 数据匹配
data_end = pd.merge(left=data_repeat, right=data2, on=['set', 'choice_card'], how='left')
# 数据导出
data_end.to_excel("C:\\Users\\CYH10\\Desktop\\end.xlsx", index=False)
