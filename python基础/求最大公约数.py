def g(m,n):
    if m<n:
        m,n=n,m
    r=m%n
    while r!=0:
        m=n
        n=r
        r=m%n
    return n
a=input()
a=a.split(' ')
d=eval(a[0])
e=eval(a[1])
print(g(d,e))
