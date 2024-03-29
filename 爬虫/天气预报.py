import requests
from lxml import etree

url = "https://www.msn.cn/zh-cn/weather/forecast/in-安徽省,合肥市"
resp = requests.get(url)
htm = etree.HTML(resp.text)
lis = htm.xpath('/html/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/ul/li')
print(lis)
for i in lis:
    a=i.xpath("./button/span/div/p/text()")
    print(a)
