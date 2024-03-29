import requests
from bs4 import BeautifulSoup

def get_baidu_search_results(keyword):
    url = f"https://www.baidu.com/s?wd={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        result_tag = soup.find('span', class_='nums')
        if result_tag:
            result_text = result_tag.get_text()
            result_count = int(''.join(filter(str.isdigit, result_text)))
            return result_count
        else:
            return None
    else:
        return None

keyword = input("请输入要搜索的关键词：")
result_count = get_baidu_search_results(keyword)
if result_count is not None:
    print(f"关键词 '{keyword}' 的搜索结果约有 {result_count} 个。")
else:
    print("无法获取搜索结果。")