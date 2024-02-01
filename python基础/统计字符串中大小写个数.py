s=input()
a=0
b=0
for i in s:
    if i.isupper():
        a+=1
    if i.islower():
        b+=1
print("大写",a,   "小写",b)