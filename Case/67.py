import pandas as pd
import openpyxl

# 读取Excel文件
df = pd.read_excel("..\\Case\\data\\按键选择.xlsx")

new_df = openpyxl.Workbook()
sheet = new_df.create_sheet('sheet1')
table = new_df.active
for i in range(200):
    a = list(df.iloc[0+10*i: 10*(i+1), -1])
    table.append(a)

new_df.save("output.xlsx")
d = []
df = pd.read_excel("output.xlsx")
for i in range(10):
    num_1 = 0
    num_2 = 0
    num_3 = 0
    num_4 = 0
    v = []
    a = list(df.iloc[0: -1, i])
    for j in a:
        if j == 1:
            num_1 += 1
        if j == 2:
            num_2 += 1
        if j == 3:
            num_3 += 1
        if j == 4:
            num_4 += 1
    v.append(num_1)
    v.append(num_2)
    v.append(num_3)
    v.append(num_4)
    d.append(v)
print(d)

