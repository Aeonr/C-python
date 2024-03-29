a = input()
b = []
for i in range(5):
    b.append(int(a[i]))
for k in range(5):
    b[k] = (b[k] + 8) % 7
b[0], b[4] = b[4], b[0]
b[1], b[2] = b[2], b[1]
for j in range(5):
    print(b[j], end='')
