import requests
from pyquery import PyQuery
def get_page_source(url):
    resp=requests.post(url)
    resp.encoding="utf-8"
    return resp.text
def parse_page_source(html):
    doc=PyQuery(html)
    doc("")

def main():
    url="https://k.autohome.com.cn/146/"
    html=get_page_source(url)
    parse_page_source(html)
