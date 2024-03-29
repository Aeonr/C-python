import requests
import re
domain="https://www.dytt89.com/"
resp=requests.get(domain,verify=False) #verify去掉安全验证
resp.encoding='gb2312'
print(resp.text)
obj1=re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S) #a标签表示超链接 例<a href='url'>周杰伦</a> 点击周杰伦后会跳转到href中的url
obj2=re.compile(r"<a href='(?P<href>.*?)'")#提取子页面链接
obj3=re.compile(r'◎片　　名(?P<name>.*?)<br />.*?<li><a href="(?P<download>.*?)">',re.S)
result1=obj1.finditer(resp.text)
child_href_list=[]
for i in result1:
    ul=i.group('ul')
    result2=obj2.finditer(ul)
    for j in result2:
        child_href=domain+j.group('href').strip("/") #拼接域名和子页面网址
        child_href_list.append(child_href)
for href in child_href_list:
    resp1=requests.get(href,verify=False)
    resp1.encoding='gb2312'
    print(resp1.text)
    result3=obj3.search(resp1.text)
    print(result3.group("name"))
    print(result3.group("download"))




