import requests
a=eval(input("你想要查询的起始位置："))
url="https://movie.douban.com/j/chart/top_list"
param={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": a-1,
    "limit": 20
}
        #代码封装，问号后的字符用负载中的值进行代替param
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"}
resp=requests.get(url=url,params=param,headers=header)
print(resp.json())
resp.close()