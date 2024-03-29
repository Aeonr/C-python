def f(a):
    b=[1,1]
    c=2
    for i in range(2,a+1):
        s=b[i-1]+b[i-2]
        b.append(s)
        c=c+b[i]
    print(c)
f(4)