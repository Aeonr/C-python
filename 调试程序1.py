import requests
import re
import time
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }


def set_link(year):
    # year参数为需要爬取数据的年份
    link = []
    for i in range(1, 13):
        # 一年有12个月份
        if i < 10:
            url = 'http://lishi.tianqi.com/mianyang/{}0{}.html'.format(year, i)
        else:
            url = 'http://lishi.tianqi.com/mianyang/{}{}.html'.format(year, i)
        link.append(url)
    return link


def get_page(url, headers):
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        html.encoding = html.apparent_encoding
        return html.text
    else:
        return None


date_box = []
max_temp = []
min_temp = []
weh = []
wind = []
week_box = []


def get_data():
    link = set_link(2019)
    for url in link:
        html = get_page(url, headers)
        bs = BeautifulSoup(html, 'html.parser')

        data = bs.find_all(class_='thrui')
        date = re.compile('class="th200">(.*?)</')
        tem = re.compile('class="th140">(.*?)</')
        time = re.findall(date, str(data))
        print(time)
        print(len(time))
        for item in time:
            week = item[10:]
            week_box.append(week)
            date_box.append(item[:10])
        temp = re.findall(tem, str(data))
        for i in range(len(time)):
            # 之前因为自身需要的只是19年6月的天气信息，没有考虑到每个月的天数不一样，现在修改后就没有问题了
            max_temp.append(temp[i * 4 + 0])
            min_temp.append(temp[i * 4 + 1])
            weh.append(temp[i * 4 + 2])
            wind.append(temp[i * 4 + 3])


get_data()
datas = pd.DataFrame(
    {'日期': date_box, '星期': week_box, '最高温度': max_temp, '最低温度': min_temp, '天气': weh, '风向': wind})
datas.to_csv('D:\\天气数据.csv', encoding='utf_8_sig')
print(datas)
