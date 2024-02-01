import pandas as pd
import xlwt

d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2014.xlsx', header=0)
data = d['咸阳日径流']
y = d['年']
m = d['月']
r = d['日']
s = []

for i in range(len(data)):
    b = str(m[i]) + '/' + str(r[i]) + '/' + str(y[i])
    c = []
    c.append(b)
    c.append(data[i])
    s.append(c)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('咸阳站', cell_overwrite_ok=True)
col = ('data', 'flow')

for i in range(0, 2):
    sheet.write(0, i, col[i])

for i in range(len(s)):
    data = s[i]
    for j in range(0, 2):
        sheet.write(i + 1, j, data[j])

savepath = 'E:\\建模比赛\\xy1979coutput.xls'
book.save(savepath)
