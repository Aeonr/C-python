def to_array(x):
    list = []
    for i in  range(4):
        a=x%10
        list.append(a)
        x=int(x/10)
    return list

def  to_number(list):num
    num=0
    for i in range(4):
        num=num*10+list[i]
    return num

x=eval(input("请输入一个四位数："))
while True:
    list=to_array(x)
    list.sort()
    min=to_number(list)
    list.sort(reverse=True)
    max=to_number(list)
    x=max-min
    print(max,'-',min,'=',x)
    if (x==0 or x==6174):
        break