import lxml
import requests
from lxml import etree
from lxml import html
import csv

def getWeather(url):
    # 请求头信息:浏览器版本型号,接收数据的编码格式
    headers = {
        # 必填,不填拿不到数据
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    # 请求 接收到了响应数据
    resp = requests.get(url, headers=headers)

    # 使用lxml解析HTML
    tree = lxml.html.fromstring(resp.text)
    resp_list = tree.xpath("//ul[@class='thrui']/li")

    # for循环迭代遍历
    day_weather_info = []
    for li in resp_list:
        dates = li.xpath('.//div[@class="th200"]/text()')  # 提取日期
        max_temperatures = li.xpath('.//div[@class="th140"]/text()')  # 提取最高气温
        min_temperatures = li.xpath('.//div[@class="th140"][2]/text()')  # 提取最低气温
        weather_conditions = li.xpath('.//div[@class="th140"][3]/text()')  # 提取天气情况
        wind_directions = li.xpath('.//div[@class="th140"][4]/text()')[0].split(' ')[0]  # 提取风向
        wind_speeds = li.xpath('.//div[@class="th140"][4]/text()')[0].split(' ')[1]  # 提取风速

        # 将提取的信息存储到day_weather_info列表中
        day_weather_info.append({
            "日期": dates[0],
            "最高气温": max_temperatures[0],
            "最低气温": min_temperatures[0],
            "天气情况": weather_conditions[0],
            "风向": wind_directions,
            "风速": wind_speeds
        })
    return day_weather_info


weathers = [getWeather(f'https://lishi.tianqi.com/dongguan/2023{str(month).zfill(2)}.html') for month in range(1, 13)]
print(weathers)

# 数据写入(一次性写入)
with open("test01_weather.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入列名:columns_name 日期 最高气温 最低气温  天气
    writer.writerow(["日期", "最高气温", "最低气温", '天气', "风向", "风速"])
    # 一次写入多行用writerows(写入的数据类型是列表,一个列表对应一行)
    writer.writerows(
        [list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])
print("写入成功！")
