import requests
from bs4 import BeautifulSoup
url="https://www.pearvideo.com/video_1773234"
resp=requests.get(url)
page=BeautifulSoup(resp.text,"html.parser")
V=page.find("video",style='')
print(V)
src=V.get('src')
resp1=requests.get(src)
print(resp1.text)