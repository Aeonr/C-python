import re
#findall:匹配字符串中所有符合正则的内容
list=re.findall(r"\d+","我的电话是10086")
print(list)
#finditer：匹配字符串中所有的内容(返回迭代器）,从迭代器拿内容需要.group()
it=re.finditer(r"\d+","我的电话是10086")
for i in it:
    print(i.group())
#search返回的结果是match对象，找到一个结果就返回，拿数据需要.group(),
s=re.search(r"\d+","我的电话是10086")
print(s.group())
#match从头开始匹配，一开始找不到就报错
s=re.match(r"\d+","10086")
print(s.group())
#数据预处理预加载
obj=re.compile(r"\d+")
r=obj.finditer("我的电话是10086")
for i in r:
    print(i.group())



s="""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说</span></div>
"""
obj=re.compile(r"<div class='(?P<name>.*?)'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)#让.能匹配换行符 \ (?P<元组名称>)
result=obj.finditer(s)
for it in result:
    print(it.group("name"))
    print(it.group("id"))
    print(it.group("wahaha"))
