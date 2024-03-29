import requests
a=input()
url="https://www.sogou.com/web?query={a}"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"}
resp=requests.get(url,headers=headers)#请求头反爬
print(resp)
print(resp.text)
resp.close()