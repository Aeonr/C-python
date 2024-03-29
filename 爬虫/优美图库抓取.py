import requests
from bs4 import BeautifulSoup
import time #使请求间隔变长
url="http://www.umeituku.com/bizhitupian/weimeibizhi/"
resp=requests.get(url)
resp.encoding='utf-8'
page=BeautifulSoup(resp.text,"html.parser")
alist=page.find("div",class_="TypeList").find_all("a")
for a in alist:
    href=a.get('href')
    resp1=requests.get(href)  #.get拿属性值
    resp1.encoding='utf-8'
    page2=BeautifulSoup(resp1.text,"html.parser")
    div=page2.find("div",class_="ImageBody")
    img=div.find("img")
    src=img.get("src")
    resp2=requests.get(src)
    resp2.content   #拿到所有字节
    img_name=src.split("/")[-1]  #拿到url最后一个杠后面的内容
    with open("img/"+img_name,mode="wb") as f:
        f.write(resp2.content)
        time.sleep(1)
    f.close()
resp.close()
print("over")