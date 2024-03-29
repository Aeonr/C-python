import  requests
from lxml import etree
url="https://hefei.zbj.com/search/service?kw=saas&r=1"
resp=requests.get(url)
html=etree.HTML(resp.text)

divs=html.xpath("/html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div")

for i in divs:
    p=i.xpath("./div[3]/div/span[1]/text()")
    print(p)