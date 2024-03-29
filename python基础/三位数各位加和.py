a = eval(input("请随机输入一个三位数："))
b = a // 100
c = (a - 100) // 10
d = a - b * 100 - c * 10
e = b + c + d
print(e)

