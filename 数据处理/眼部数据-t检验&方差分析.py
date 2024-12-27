import pandas as pd
from scipy.stats import ttest_ind, levene, normaltest, ttest_rel, f_oneway, kruskal
import numpy as np

diopter = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='屈光度')
axial = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='眼轴长')
choroid = pd.read_excel(r'..\Case\使用记录.xlsx', sheet_name='脉络膜厚度')

diopter_feeder_base = diopter.loc[diopter['组别'] == '哺光仪组', '基线数据'].agg(list)
diopter_feeder_1 = diopter.loc[diopter['组别'] == '哺光仪组', '第一次复查'].agg(list)
diopter_feeder_1 = [x - (-3.51) for x in diopter_feeder_1]
diopter_feeder_2 = diopter.loc[diopter['组别'] == '哺光仪组', '第二次复查'].agg(list)
diopter_feeder_2 = [x - (-3.51) for x in diopter_feeder_2]
diopter_feeder_3 = diopter.loc[diopter['组别'] == '哺光仪组', '第三次复查'].agg(list)
diopter_feeder_3 = [x - (-3.51) for x in diopter_feeder_3]
diopter_feeder_4 = diopter.loc[diopter['组别'] == '哺光仪组', '第四次复查'].agg(list)
diopter_feeder_4 = [x - (-3.51) for x in diopter_feeder_4]

diopter_cnc_base = diopter.loc[diopter['组别'] == 'CNC组', '基线数据'].agg(list)
diopter_cnc_1 = diopter.loc[diopter['组别'] == 'CNC组', '第一次复查'].agg(list)
diopter_cnc_1 = [x - (-1.75) for x in diopter_cnc_1]
diopter_cnc_2 = diopter.loc[diopter['组别'] == 'CNC组', '第二次复查'].agg(list)
diopter_cnc_2 = [x - (-1.75) for x in diopter_cnc_2]
diopter_cnc_3 = diopter.loc[diopter['组别'] == 'CNC组', '第三次复查'].agg(list)
diopter_cnc_3 = [x - (-1.75) for x in diopter_cnc_3]
diopter_cnc_4 = diopter.loc[diopter['组别'] == 'CNC组', '第四次复查'].agg(list)
diopter_cnc_4 = [x - (-1.75) for x in diopter_cnc_4]

diopter_con_base = diopter.loc[diopter['组别'] == '对照组', '基线数据'].agg(list)
diopter_con_1 = diopter.loc[diopter['组别'] == '对照组', '第一次复查'].agg(list)
diopter_con_1 = [x - (-2.03) for x in diopter_con_1]
diopter_con_2 = diopter.loc[diopter['组别'] == '对照组', '第二次复查'].agg(list)
diopter_con_2 = [x - (-2.03) for x in diopter_con_2]
diopter_con_3 = diopter.loc[diopter['组别'] == '对照组', '第三次复查'].agg(list)
diopter_con_3 = [x - (-2.03) for x in diopter_con_3]
diopter_con_4 = diopter.loc[diopter['组别'] == '对照组', '第四次复查'].agg(list)
diopter_con_4 = [x - (-2.03) for x in diopter_con_4]

axial_feeder_base = axial.loc[axial['组别'] == '哺光仪组', '基线数据'].agg(list)
axial_feeder_1 = axial.loc[axial['组别'] == '哺光仪组', '第一次复查'].agg(list)
axial_feeder_1 = [x - 24.85 for x in axial_feeder_1]
axial_feeder_2 = axial.loc[axial['组别'] == '哺光仪组', '第二次复查'].agg(list)
axial_feeder_2 = [x - 24.85 for x in axial_feeder_2]
axial_feeder_3 = axial.loc[axial['组别'] == '哺光仪组', '第三次复查'].agg(list)
axial_feeder_3 = [x - 24.85 for x in axial_feeder_3]
axial_feeder_4 = axial.loc[axial['组别'] == '哺光仪组', '第四次复查'].agg(list)
axial_feeder_4 = [x - 24.85 for x in axial_feeder_4]

axial_cnc_base = axial.loc[axial['组别'] == 'CNC组', '基线数据'].agg(list)
axial_cnc_1 = axial.loc[axial['组别'] == 'CNC组', '第一次复查'].agg(list)
axial_cnc_1 = [x - 23.81 for x in axial_cnc_1]
axial_cnc_2 = axial.loc[axial['组别'] == 'CNC组', '第二次复查'].agg(list)
axial_cnc_2 = [x - 23.81 for x in axial_cnc_2]
axial_cnc_3 = axial.loc[axial['组别'] == 'CNC组', '第三次复查'].agg(list)
axial_cnc_3 = [x - 23.81 for x in axial_cnc_3]
axial_cnc_4 = axial.loc[axial['组别'] == 'CNC组', '第四次复查'].agg(list)
axial_cnc_4 = [x - 23.81 for x in axial_cnc_4]

axial_con_base = axial.loc[axial['组别'] == '对照组', '基线数据'].agg(list)
axial_con_1 = axial.loc[axial['组别'] == '对照组', '第一次复查'].agg(list)
axial_con_1 = [x - 24.31 for x in axial_con_1]
axial_con_2 = axial.loc[axial['组别'] == '对照组', '第二次复查'].agg(list)
axial_con_2 = [x - 24.31 for x in axial_con_2]
axial_con_3 = axial.loc[axial['组别'] == '对照组', '第三次复查'].agg(list)
axial_con_3 = [x - 24.31 for x in axial_con_3]
axial_con_4 = axial.loc[axial['组别'] == '对照组', '第四次复查'].agg(list)
axial_con_4 = [x - 24.31 for x in axial_con_4]

choroid_feeder_base = choroid.loc[choroid['组别'] == '哺光仪组', '基线数据'].agg(list)
choroid_feeder_1 = choroid.loc[choroid['组别'] == '哺光仪组', '第一次复查'].agg(list)
choroid_feeder_1 = [x - 268.35 for x in choroid_feeder_1]
choroid_feeder_2 = choroid.loc[choroid['组别'] == '哺光仪组', '第二次复查'].agg(list)
choroid_feeder_2 = [x - 268.35 for x in choroid_feeder_2]
choroid_feeder_3 = choroid.loc[choroid['组别'] == '哺光仪组', '第三次复查'].agg(list)
choroid_feeder_3 = [x - 268.35 for x in choroid_feeder_3]
choroid_feeder_4 = choroid.loc[choroid['组别'] == '哺光仪组', '第四次复查'].agg(list)
choroid_feeder_4 = [x - 268.35 for x in choroid_feeder_4]

choroid_cnc_base = choroid.loc[choroid['组别'] == 'CNC组', '基线数据'].agg(list)
choroid_cnc_1 = choroid.loc[choroid['组别'] == 'CNC组', '第一次复查'].agg(list)
choroid_cnc_1 = [x - 302.5 for x in choroid_cnc_1]
choroid_cnc_2 = choroid.loc[choroid['组别'] == 'CNC组', '第二次复查'].agg(list)
choroid_cnc_2 = [x - 302.5 for x in choroid_cnc_2]
choroid_cnc_3 = choroid.loc[choroid['组别'] == 'CNC组', '第三次复查'].agg(list)
choroid_cnc_3 = [x - 302.5 for x in choroid_cnc_3]
choroid_cnc_4 = choroid.loc[choroid['组别'] == 'CNC组', '第四次复查'].agg(list)
choroid_cnc_4 = [x - 302.5 for x in choroid_cnc_4]

choroid_con_base = choroid.loc[choroid['组别'] == '对照组', '基线数据'].agg(list)
choroid_con_1 = choroid.loc[choroid['组别'] == '对照组', '第一次复查'].agg(list)
choroid_con_1 = [x - 314.05 for x in choroid_con_1]
choroid_con_2 = choroid.loc[choroid['组别'] == '对照组', '第二次复查'].agg(list)
choroid_con_2 = [x - 314.05 for x in choroid_con_2]
choroid_con_3 = choroid.loc[choroid['组别'] == '对照组', '第三次复查'].agg(list)
choroid_con_3 = [x - 314.05 for x in choroid_con_3]
choroid_con_4 = choroid.loc[choroid['组别'] == '对照组', '第四次复查'].agg(list)
choroid_con_4 = [x - 314.05 for x in choroid_con_4]

value_list = [diopter_feeder_base, diopter_feeder_1, diopter_feeder_2, diopter_feeder_3, diopter_feeder_4,
              diopter_cnc_base, diopter_cnc_1, diopter_cnc_2, diopter_cnc_3, diopter_cnc_4,
              diopter_con_base, diopter_con_1, diopter_con_2, diopter_con_3, diopter_con_4,
              axial_feeder_base, axial_feeder_1, axial_feeder_2, axial_feeder_3, axial_feeder_4,
              axial_cnc_base, axial_cnc_1, axial_cnc_2, axial_cnc_3, axial_cnc_4,
              axial_con_base, axial_con_1, axial_con_2, axial_con_3, axial_con_4,
              choroid_feeder_base, choroid_feeder_1, choroid_feeder_2, choroid_feeder_3, choroid_feeder_4,
              choroid_cnc_base, choroid_cnc_1, choroid_cnc_2, choroid_cnc_3, choroid_cnc_4,
              choroid_con_base, choroid_con_1, choroid_con_2, choroid_con_3, choroid_con_4]
value_list_name = ['diopter_feeder_base', 'diopter_feeder_1', 'diopter_feeder_2', 'diopter_feeder_3', 'diopter_feeder_4',
                   'diopter_cnc_base', 'diopter_cnc_1', 'diopter_cnc_2', 'diopter_cnc_3', 'diopter_cnc_4',
                   'diopter_con_base', 'diopter_con_1', 'diopter_con_2', 'diopter_con_3', 'diopter_con_4',
                   'axial_feeder_base', 'axial_feeder_1', 'axial_feeder_2', 'axial_feeder_3', 'axial_feeder_4',
                   'axial_cnc_base', 'axial_cnc_1', 'axial_cnc_2', 'axial_cnc_3', 'axial_cnc_4',
                   'axial_con_base', 'axial_con_1', 'axial_con_2', 'axial_con_3', 'axial_con_4',
                   'choroid_feeder_base', 'choroid_feeder_1', 'choroid_feeder_2', 'choroid_feeder_3', 'choroid_feeder_4',
                   'choroid_cnc_base', 'choroid_cnc_1', 'choroid_cnc_2', 'choroid_cnc_3', 'choroid_cnc_4',
                   'choroid_con_base', 'choroid_con_1', 'choroid_con_2', 'choroid_con_3', 'choroid_con_4']

# 正态性检验
p_value_list = {}
for i in range(len(value_list)):
    p_value = normaltest(value_list[i])[1]
    p_value_list[value_list_name[i]] = p_value
p_value_list = {k: round(v, 2) for k, v in p_value_list.items()}
# print(p_value_list)  # 正态性阈值0.05，大于0.05认为是正态

# 标准差 & 方差
desc = {}
for i in range(len(value_list)):
    desc[value_list_name[i]] = np.mean(value_list[i]), np.std(value_list[i])
desc = {k: tuple(round(x, 2) for x in v) for k, v in desc.items()}
print(desc)

# 组间比较
# 两组间独立样本t检验
# 屈光度
t_result_diopter = {}
s, f = ttest_ind(diopter_feeder_base, diopter_con_base)
t_result_diopter['diopter_feeder_con_base'] = s, f
s, f = ttest_ind(diopter_cnc_base, diopter_con_base)
t_result_diopter['diopter_cnc_con_base'] = s, f
s, f = ttest_ind(diopter_feeder_1, diopter_con_1)
t_result_diopter['diopter_feeder_con_1'] = s, f
s, f = ttest_ind(diopter_cnc_1, diopter_con_1)
t_result_diopter['diopter_cnc_con_1'] = s, f
s, f = ttest_ind(diopter_feeder_2, diopter_con_2)
t_result_diopter['diopter_feeder_con_2'] = s, f
s, f = ttest_ind(diopter_cnc_2, diopter_con_2)
t_result_diopter['diopter_cnc_con_2'] = s, f
s, f = ttest_ind(diopter_feeder_3, diopter_con_3)
t_result_diopter['diopter_feeder_con_3'] = s, f
s, f = ttest_ind(diopter_cnc_3, diopter_con_3)
t_result_diopter['diopter_cnc_con_3'] = s, f
s, f = ttest_ind(diopter_feeder_4, diopter_con_4)
t_result_diopter['diopter_feeder_con_4'] = s, f
s, f = ttest_ind(diopter_cnc_4, diopter_con_4)
t_result_diopter['diopter_cnc_con_4'] = s, f
t_result_diopter = {k: tuple(round(x, 2) for x in v) for k, v in t_result_diopter.items()}
print(t_result_diopter)  # t检验阈值0.05，小于0.05认为是显著
# 眼轴长
t_result_axial = {}
s, f = ttest_ind(axial_feeder_base, axial_con_base)
t_result_axial['axial_feeder_con_base'] = s, f
s, f = ttest_ind(axial_cnc_base, axial_con_base)
t_result_axial['axial_cnc_con_base'] = s, f
s, f = ttest_ind(axial_feeder_1, axial_con_1)
t_result_axial['axial_feeder_con_1'] = s, f
s, f = ttest_ind(axial_cnc_1, axial_con_1)
t_result_axial['axial_cnc_con_1'] = s, f
s, f = ttest_ind(axial_feeder_2, axial_con_2)
t_result_axial['axial_feeder_con_2'] = s, f
s, f = ttest_ind(axial_cnc_2, axial_con_2)
t_result_axial['axial_cnc_con_2'] = s, f
s, f = ttest_ind(axial_feeder_3, axial_con_3)
t_result_axial['axial_feeder_con_3'] = s, f
s, f = ttest_ind(axial_cnc_3, axial_con_3)
t_result_axial['axial_cnc_con_3'] = s, f
s, f = ttest_ind(axial_feeder_4, axial_con_4)
t_result_axial['axial_feeder_con_4'] = s, f
s, f = ttest_ind(axial_cnc_4, axial_con_4)
t_result_axial['axial_cnc_con_4'] = s, f
t_result_axial = {k: tuple(round(x, 2) for x in v) for k, v in t_result_axial.items()}
print(t_result_axial)
# 脉络膜
t_result_choroid = {}
s, f = ttest_ind(choroid_feeder_base, choroid_con_base)
t_result_choroid['choroid_feeder_con_base'] = s, f
s, f = ttest_ind(choroid_cnc_base, choroid_con_base)
t_result_choroid['choroid_cnc_con_base'] = s, f
s, f = ttest_ind(choroid_feeder_1, choroid_con_1)
t_result_choroid['choroid_feeder_con_1'] = s, f
s, f = ttest_ind(choroid_cnc_1, choroid_con_1)
t_result_choroid['choroid_cnc_con_1'] = s, f
s, f = ttest_ind(choroid_feeder_2, choroid_con_2)
t_result_choroid['choroid_feeder_con_2'] = s, f
s, f = ttest_ind(choroid_cnc_2, choroid_con_2)
t_result_choroid['choroid_cnc_con_2'] = s, f
s, f = ttest_ind(choroid_feeder_3, choroid_con_3)
t_result_choroid['choroid_feeder_con_3'] = s, f
s, f = ttest_ind(choroid_cnc_3, choroid_con_3)
t_result_choroid['choroid_cnc_con_3'] = s, f
s, f = ttest_ind(choroid_feeder_4, choroid_con_4)
t_result_choroid['choroid_feeder_con_4'] = s, f
s, f = ttest_ind(choroid_cnc_4, choroid_con_4)
t_result_choroid['choroid_cnc_con_4'] = s, f
t_result_choroid = {k: tuple(round(x, 2) for x in v) for k, v in t_result_choroid.items()}
print(t_result_choroid)

# 组内比较
# 组内配对样本t检验
diopter_feeder_result = {}
s, f = ttest_rel(diopter_feeder_base, diopter_feeder_1)
diopter_feeder_result['diopter_feeder_1'] = s, f
s, f = ttest_rel(diopter_feeder_base, diopter_feeder_2)
diopter_feeder_result['diopter_feeder_2'] = s, f
s, f = ttest_rel(diopter_feeder_base, diopter_feeder_3)
diopter_feeder_result['diopter_feeder_3'] = s, f
s, f = ttest_rel(diopter_feeder_base, diopter_feeder_4)
diopter_feeder_result['diopter_feeder_4'] = s, f
diopter_feeder_result = {k: tuple(round(x, 2) for x in v) for k, v in diopter_feeder_result.items()}
# print(diopter_feeder_result)

diopter_cnc_result = {}
s, f = ttest_rel(diopter_cnc_base, diopter_cnc_1)
diopter_cnc_result['diopter_cnc_1'] = s, f
s, f = ttest_rel(diopter_cnc_base, diopter_cnc_2)
diopter_cnc_result['diopter_cnc_2'] = s, f
s, f = ttest_rel(diopter_cnc_base, diopter_cnc_3)
diopter_cnc_result['diopter_cnc_3'] = s, f
s, f = ttest_rel(diopter_cnc_base, diopter_cnc_4)
diopter_cnc_result['diopter_cnc_4'] = s, f
diopter_cnc_result = {k: tuple(round(x, 2) for x in v) for k, v in diopter_cnc_result.items()}
# print(diopter_cnc_result)

diopter_con_result = {}
s, f = ttest_rel(diopter_con_base, diopter_con_1)
diopter_con_result['diopter_con_1'] = s, f
s, f = ttest_rel(diopter_con_base, diopter_con_2)
diopter_con_result['diopter_con_2'] = s, f
s, f = ttest_rel(diopter_con_base, diopter_con_3)
diopter_con_result['diopter_con_3'] = s, f
s, f = ttest_rel(diopter_con_base, diopter_con_4)
diopter_con_result['diopter_con_4'] = s, f
diopter_con_result = {k: tuple(round(x, 2) for x in v) for k, v in diopter_con_result.items()}
# print(diopter_con_result)

axial_feeder_result = {}
s, f = ttest_rel(axial_feeder_base, axial_feeder_1)
axial_feeder_result['axial_feeder_1'] = s, f
s, f = ttest_rel(axial_feeder_base, axial_feeder_2)
axial_feeder_result['axial_feeder_2'] = s, f
s, f = ttest_rel(axial_feeder_base, axial_feeder_3)
axial_feeder_result['axial_feeder_3'] = s, f
s, f = ttest_rel(axial_feeder_base, axial_feeder_4)
axial_feeder_result['axial_feeder_4'] = s, f
axial_feeder_result = {k: tuple(round(x, 2) for x in v) for k, v in axial_feeder_result.items()}
# print(axial_feeder_result)

axial_cnc_result = {}
s, f = ttest_rel(axial_cnc_base, axial_cnc_1)
axial_cnc_result['axial_cnc_1'] = s, f
s, f = ttest_rel(axial_cnc_base, axial_cnc_2)
axial_cnc_result['axial_cnc_2'] = s, f
s, f = ttest_rel(axial_cnc_base, axial_cnc_3)
axial_cnc_result['axial_cnc_3'] = s, f
s, f = ttest_rel(axial_cnc_base, axial_cnc_4)
axial_cnc_result['axial_cnc_4'] = s, f
axial_cnc_result = {k: tuple(round(x, 2) for x in v) for k, v in axial_cnc_result.items()}
# print(axial_cnc_result)

axial_con_result = {}
s, f = ttest_rel(axial_con_base, axial_con_1)
axial_con_result['axial_con_1'] = s, f
s, f = ttest_rel(axial_con_base, axial_con_2)
axial_con_result['axial_con_2'] = s, f
s, f = ttest_rel(axial_con_base, axial_con_3)
axial_con_result['axial_con_3'] = s, f
s, f = ttest_rel(axial_con_base, axial_con_4)
axial_con_result['axial_con_4'] = s, f
axial_con_result = {k: tuple(round(x, 2) for x in v) for k, v in axial_con_result.items()}
# print(axial_con_result)

choroid_feeder_result = {}
s, f = ttest_rel(choroid_feeder_base, choroid_feeder_1)
choroid_feeder_result['choroid_feeder_1'] = s, f
s, f = ttest_rel(choroid_feeder_base, choroid_feeder_2)
choroid_feeder_result['choroid_feeder_2'] = s, f
s, f = ttest_rel(choroid_feeder_base, choroid_feeder_3)
choroid_feeder_result['choroid_feeder_3'] = s, f
s, f = ttest_rel(choroid_feeder_base, choroid_feeder_4)
choroid_feeder_result['choroid_feeder_4'] = s, f
choroid_feeder_result = {k: tuple(round(x, 2) for x in v) for k, v in choroid_feeder_result.items()}
# print(choroid_feeder_result)

choroid_cnc_result = {}
s, f = ttest_rel(choroid_cnc_base, choroid_cnc_1)
choroid_cnc_result['choroid_cnc_1'] = s, f
s, f = ttest_rel(choroid_cnc_base, choroid_cnc_2)
choroid_cnc_result['choroid_cnc_2'] = s, f
s, f = ttest_rel(choroid_cnc_base, choroid_cnc_3)
choroid_cnc_result['choroid_cnc_3'] = s, f
s, f = ttest_rel(choroid_cnc_base, choroid_cnc_4)
choroid_cnc_result['choroid_cnc_4'] = s, f
choroid_cnc_result = {k: tuple(round(x, 2) for x in v) for k, v in choroid_cnc_result.items()}
# print(choroid_cnc_result)

choroid_con_result = {}
s, f = ttest_rel(choroid_con_base, choroid_con_1)
choroid_con_result['choroid_con_1'] = s, f
s, f = ttest_rel(choroid_con_base, choroid_con_2)
choroid_con_result['choroid_con_2'] = s, f
s, f = ttest_rel(choroid_con_base, choroid_con_3)
choroid_con_result['choroid_con_3'] = s, f
s, f = ttest_rel(choroid_con_base, choroid_con_4)
choroid_con_result['choroid_con_4'] = s, f
choroid_con_result = {k: tuple(round(x, 2) for x in v) for k, v in choroid_con_result.items()}
# print(choroid_con_result)

# 组间K-W检验
k_diopter = {}
stat, p = kruskal(diopter_feeder_base, diopter_cnc_base, diopter_con_base)
k_diopter['base'] = stat, p
stat, p = kruskal(diopter_feeder_1, diopter_cnc_1, diopter_con_1)
k_diopter['1'] = stat, p
stat, p = kruskal(diopter_feeder_2, diopter_cnc_2, diopter_con_2)
k_diopter['2'] = stat, p
stat, p = kruskal(diopter_feeder_3, diopter_cnc_3, diopter_con_3)
k_diopter['3'] = stat, p
stat, p = kruskal(diopter_feeder_4, diopter_cnc_4, diopter_con_4)
k_diopter['4'] = stat, p
k_diopter = {k: tuple(round(x, 2) for x in v) for k, v in k_diopter.items()}
print(k_diopter)

k_axial = {}
stat, p = kruskal(axial_feeder_base, axial_cnc_base, axial_con_base)
k_axial['base'] = stat, p
stat, p = kruskal(axial_feeder_1, axial_cnc_1, axial_con_1)
k_axial['1'] = stat, p
stat, p = kruskal(axial_feeder_2, axial_cnc_2, axial_con_2)
k_axial['2'] = stat, p
stat, p = kruskal(axial_feeder_3, axial_cnc_3, axial_con_3)
k_axial['3'] = stat, p
stat, p = kruskal(axial_feeder_4, axial_cnc_4, axial_con_4)
k_axial['4'] = stat, p
k_axial = {k: tuple(round(x, 2) for x in v) for k, v in k_axial.items()}
print(k_axial)

k_choroid = {}
stat, p = kruskal(choroid_feeder_base, choroid_cnc_base, choroid_con_base)
k_choroid['base'] = stat, p
stat, p = kruskal(choroid_feeder_1, choroid_cnc_1, choroid_con_1)
k_choroid['1'] = stat, p
stat, p = kruskal(choroid_feeder_2, choroid_cnc_2, choroid_con_2)
k_choroid['2'] = stat, p
stat, p = kruskal(choroid_feeder_3, choroid_cnc_3, choroid_con_3)
k_choroid['3'] = stat, p
stat, p = kruskal(choroid_feeder_4, choroid_cnc_4, choroid_con_4)
k_choroid['4'] = stat, p
k_choroid = {k: tuple(round(x, 2) for x in v) for k, v in k_choroid.items()}
print(k_choroid)

# 组内方差分析
anova_diopter = {}
f, p = f_oneway(diopter_feeder_1, diopter_feeder_2, diopter_feeder_3, diopter_feeder_4)
anova_diopter['feeder'] = f, p
f, p = f_oneway(diopter_cnc_1, diopter_cnc_2, diopter_cnc_3, diopter_cnc_4)
anova_diopter['cnc'] = f, p
f, p = f_oneway(diopter_con_1, diopter_con_2, diopter_con_3, diopter_con_4)
anova_diopter['con'] = f, p
anova_diopter = {k: tuple(round(x, 2) for x in v) for k, v in anova_diopter.items()}
# print(anova_diopter)

anova_axial = {}
f, p = f_oneway(axial_feeder_1, axial_feeder_2, axial_feeder_3, axial_feeder_4)
anova_axial['feeder'] = f, p
f, p = f_oneway(axial_cnc_1, axial_cnc_2, axial_cnc_3, axial_cnc_4)
anova_axial['cnc'] = f, p
f, p = f_oneway(axial_con_1, axial_con_2, axial_con_3, axial_con_4)
anova_axial['con'] = f, p
anova_axial = {k: tuple(round(x, 2) for x in v) for k, v in anova_axial.items()}
# print(anova_axial)

anova_choroid = {}
f, p = f_oneway(choroid_feeder_1, choroid_feeder_2, choroid_feeder_3, choroid_feeder_4)
anova_choroid['feeder'] = f, p
f, p = f_oneway(choroid_cnc_1, choroid_cnc_2, choroid_cnc_3, choroid_cnc_4)
anova_choroid['cnc'] = f, p
f, p = f_oneway(choroid_con_1, choroid_con_2, choroid_con_3, choroid_con_4)
anova_choroid['con'] = f, p
anova_choroid = {k: tuple(round(x, 2) for x in v) for k, v in anova_choroid.items()}
# print(anova_choroid)
