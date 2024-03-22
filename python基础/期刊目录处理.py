import xlwt

list = ['RT', 'SR', 'A1', 'AD', 'T1', 'JF', 'YR', 'IS', 'vo', 'OP', 'K1', 'AB', 'SN', 'DS', 'LK', 'DO']
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('sheet1')
for i in range(len(list)):
    sheet.write(0, i, list[i])
n = 1
with open("C:\\Users\\CYH10\\Desktop\\CNKI-20240128204651827.txt", encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        if len(line) != 0:
            if line[0:2] == "RT":
                sheet.write(n, 0, line[3:-1])
            if line[0:2] == "SR":
                sheet.write(n, 1, line[3:-1])
            if line[0:2] == "A1":
                sheet.write(n, 2, line[3:-1])
            if line[0:2] == "AD":
                sheet.write(n, 3, line[3:-1])
            if line[0:2] == "T1":
                sheet.write(n, 4, line[3:-1])
            if line[0:2] == "JF":
                sheet.write(n, 5, line[3:-1])
            if line[0:2] == "YR":
                sheet.write(n, 6, line[3:-1])
            if line[0:2] == "IS":
                sheet.write(n, 7, line[3:-1])
            if line[0:2] == "vo":
                sheet.write(n, 8, line[3:-1])
            if line[0:2] == "OP":
                sheet.write(n, 9, line[3:-1])
            if line[0:2] == "K1":
                sheet.write(n, 10, line[3:-1])
            if line[0:2] == "AB":
                sheet.write(n, 11, line[3:-1])
            if line[0:2] == "SN":
                sheet.write(n, 12, line[3:-1])
            if line[0:2] == "DS":
                sheet.write(n, 13, line[3:-1])
            if line[0:2] == "LK":
                sheet.write(n, 14, line[3:-1])
            if line[0:2] == "DO":
                sheet.write(n, 15, line[3:-1])
        else:
            n += 1

workbook.save('example_xlwt.xls')
