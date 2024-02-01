f=open('test.txt','r',encoding='utf-8')
t=f.read()
c=0
o=0
d=0
s=0
for i in t:
    if i.isalpha():
        c+=1
    if i.isdigit():
        d+=1
    if i.isspace():
        s+=1
    else:
        o+=1
o=o-c-d

a={}
a['character']=c
a['other']=o
a['digit']=d
a['space']=s
print(a)