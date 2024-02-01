import requests
from bs4 import BeautifulSoup
url="http://www.xinfadi.com.cn/priceDetail.html"
resp=requests.get(url)
#;把页面源代码交给beautifulsoup进行处理，生成bs4对象
page=BeautifulSoup(resp.text,"html.parser")#指定html解析器
#从bs对象中找数据
#find(标签，属性=值)
#find_all(标签，属性=值)
table=page.find("table", border="0", cellspacing="0" ,cellpadding="0")
#table=page.find("table",atters={"class":"hq_table"}) 避免关键字
#table=page.find("table"，class_="hq_table") 同上

trs=table.find_all("tr")[1:]
    ths=tr.find_all("th")
for tr in trs:
    name=ths[0].text
    lp= ths[0].text
    ap= ths[0].text
    hp = ths[0].text
    gui= ths[0].text
    place = ths[0].text
    kind= ths[0].text
    date = ths[0].text
    print(name,lp,ap,hp,gui,place,kind,date)
#该案例与教学有差异，网站源代码已发生变动，暂不处理，理解即可
