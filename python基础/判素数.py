n = eval(input())
flage = True
for i in range(2, n):
    if n % i == 0:
        flage = False
        break
if flage == True:
    print(n, "是素数")
if flage == False:
    print(n, "不是素数")
