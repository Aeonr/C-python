m = input()
l = list(m)
n = len(l)
for i in range(0, n):
    flage = True
    if l[i] != l[n - i - 1]:
        flage = False
if flage == True:
    print("Yes")
else:
    print("No")
