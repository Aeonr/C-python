import re
import requests
import csv
url="https://movie.douban.com/top250"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"}
resp=requests.get(url=url,headers=headers)
p=resp.text
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">(?P<导演主演>.*?)<br>(?P<时间>.*?)&nbsp;/&nbsp.*?<span class="rating_num" property="v:average">(?P<评分>.*?)</span>.*?<span>(?P<评价人数>.*?)</span>',re.S)
result=obj.finditer(p)

f=open("data.csv", encoding='UTF-8',mode="w")  #encoding转码
csvwriter=csv.writer(f)
for i in result:
    print(i.group("name"))
    print(i.group("导演主演").strip())
    print(i.group("时间").strip())
    print(i.group("评分").strip())
    print(i.group("评价人数").strip())
    dic=i.groupdict()
    dic['时间']=dic['时间'].strip()
    csvwriter.writerow(dic.values())
f.close()
resp.close()
print("over")