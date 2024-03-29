a = input()
b = {}
for i in a:
    if i in b:
        b[i] = b[i] + 1
    else:
        b[i] = 1
c = sorted(b.items(), key=lambda x: x[1])
d = len(c)
m = c[d - 1]
for i in range(1, d + 1):
    if c[i - 1][1] == m[1]:
        print(c[i - 1][0], c[i - 1][1])
