file1 = open('file1.txt', 'w')
n = eval(input())
for k in range(2, n + 1):
    flage = True
    for i in range(2, k):
        if k % i == 0:
            flage = False
    if flage == True:
        file1.write(str(k) + "\n")
file1.close()
