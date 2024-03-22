a = eval(input())
b = str(a)
if b == b[::-1]:
    print("是回文")
else:
    print("不是回文")
