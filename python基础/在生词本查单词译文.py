n = eval(input())
a = []
for i in range(1, n + 1):
    b = input()
    b = b.split()
    a.append(b)
c = dict(a)
d = input()
if d in c:
    print(c[d])
else:
    print("not found")
