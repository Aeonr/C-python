s = (input("请输入一个四位数："))
c = s[2]
e = eval(c)
f = eval(s)
b = f // 1000
d = b + e
if d % 2 == 0:
    print("偶数")
else:
    print("奇数")
