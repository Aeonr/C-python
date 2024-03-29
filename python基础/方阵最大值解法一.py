n=eval(input())
l=[]
m=[]
for i in range(n):
    for t in range(n):
        a=eval(input())
        l.append(a)
    m.append(l)
    l=[]
print(m,end='')
b=0
for j in range(n):
    for k in range(n):
        if m[j][k]>b:
            b=m[j][k]
print(b)
