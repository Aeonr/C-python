from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

provinces = ['陕西卫视', '江苏卫视', '东南卫视', '广东卫视', '安徽卫视',
             '北京卫视', '湖北卫视', '湖南卫视', '黑龙江卫视', '江西卫视',
             '河北卫视', '河南卫视', '山东卫视', '山西卫视', '上海卫视', '浙江卫视',
             '云南卫视', '贵州卫视', '四川卫视', '青海卫视', '甘肃卫视', '内蒙古卫视',
             '新疆卫视', '广西卫视', '宁夏卫视', '西藏卫视', '天津卫视', '辽宁卫视',
             '吉林卫视', '海南卫视', '重庆卫视']
a = []
b = []

for i in provinces:
    opt = Options()
    # opt.add_argument("--headless")     # 无头
    # opt.add_argument("--disable-gpu")  # 不可用GPU，不显示
    web = Chrome(options=opt)
    web.maximize_window()
    web.get("https://www.baidu.com/")

    input_option = web.find_element("xpath", '//*[@id="kw"]')  # element表示一个，elements表示一堆
    input_option.send_keys(f'{i} 节目 食品 食物 \n')  # 输入文字"

    WebDriverWait(web, 10, 0.5).until(EC.presence_of_element_located(('xpath', '//*[@id="tsn_inner"]/div[2]/div')))

    # 点击搜索工具
    el1 = web.find_element("xpath", '//*[@id="tsn_inner"]/div[2]/div')
    web.execute_script("arguments[0].click();", el1)

    time.sleep(2)

    # 点击时间不限
    el2 = web.find_element("xpath", '//*[@id="timeRlt"]/i')
    web.execute_script("arguments[0].click();", el2)

    time.sleep(2)

    # 输入时间起点
    el3 = web.find_element("xpath", '//*[@id="container"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/input')
    el3.clear()
    el3.send_keys('2011-01-01\n')

    # 输入时间终点
    time.sleep(1)
    el4 = web.find_element("xpath", '//*[@id="container"]/div[2]/div/div[2]/div[2]/div[3]/div[1]/input')
    el4.clear()
    el4.send_keys('2011-12-31\n')

    # 点击确定按钮
    el5 = web.find_element("xpath", '//*[@id="container"]/div[2]/div/div[2]/div[2]/div[4]/button')
    el5.click()

    time.sleep(3)

    js = "document.getElementById('tsn_inner').style.top='-42px';"
    web.execute_script(js)
    time.sleep(2)
    re = web.find_element("xpath", '//*/span[@class="hint_PIwZX c_font_2AD7M"]').text
    a.append(i)
    b.append(re)
    time.sleep(2)
    web.quit()

c = pd.DataFrame({
    "省份": a,
    "数据": b,
})
c