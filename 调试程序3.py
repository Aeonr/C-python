import requests
from lxml import etree
import pandas as pd

def get_html(place, month):
    headers = {
        "Accept-Encoding": "Gzip",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    }
    url = f'https://lishi.tianqi.com/{place}/{month}.html'

    r = requests.get(url, headers=headers)
    r_html = etree.HTML(r.text)

    return r_html


# 月份参数列表,这里需要修改时间区间的可以修改range中的数据
month_list = pd.period_range('200001', '202404', freq='M').strftime('%Y%m')

data = pd.read_excel("E:\\数据库\\数据资源整理【三】：最全中国各省份城市编码以及经纬度数据\\地市列表_拼音.xlsx")
area = data["地级市"]
area_pin = data["拼音"]
df = pd.DataFrame(columns=['地区', '日期', '最高气温', '最低气温', '天气', '风向'])
for j in range(227, len(area_pin)):
    print(area[j])
    for i, month in enumerate(month_list):
        r_html = get_html(area_pin[j], month)
        # 找到存放历史天气数据的div节点
        div = r_html.xpath('.//div[@class="tian_three"]')[0]
        # 每个日期的历史天气数据的li节点组成的列表
        lis = div.xpath('.//li')
        for li in lis:
            item = {
                '地区': area[j],
                '日期': li.xpath('./div[@class="th200"]/text()')[0],
                '最高气温': li.xpath('./div[@class="th140"]/text()')[0],
                '最低气温': li.xpath('./div[@class="th140"]/text()')[1],
                '天气': li.xpath('./div[@class="th140"]/text()')[2],
                '风向': li.xpath('./div[@class="th140"]/text()')[3]
            }
            df = df._append(item, ignore_index=True)
        print(f'{i + 1}个月数据已采集')

df.to_excel(r'历史天气数据2020.xlsx', index=None)