n = eval(input())
a = []
for i in range(n):
    i = eval(input())
    a.append(i)
b = len(a)
for i in range(b - 1):
    c = i
    for j in range(i + 1, b):
        if a[c] < a[j]:
            c = j
    a[i], a[c] = a[c], a[i]
for i in range(0, b):
    print(a[i], end=",")
