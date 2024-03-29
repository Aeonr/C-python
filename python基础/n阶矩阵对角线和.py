n = eval(input())
a = []
b = []
for i in range(n):
    for k in range(n):
        c = eval(input())
        a.append(c)
    b.append(a)
    a = []
print(b, end='')
d = 0
for i in range(n):
    for k in range(n):
        if i == k or i + k == n - 1:
            d = d + b[i][k]
print(d)
