import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from twocaptcha import TwoCaptcha
import pandas as pd

# 初始化selenium
url = 'https://wenshu.court.gov.cn/website/wenshu/181029CR4M5A62CH/index.html?'

option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 'profile.default_content_settings.popups': 0  ==  禁用弹出窗口
# 'download.default_directory': 'D:\Desktop\wenshu'  == 设置默认下载路径
# 'profile.default_content_setting_values.automatic_downloads': 1 == 并设置自动下载的选项
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': 'D:\wenshu',		# 设置自己的下载路径
         'profile.default_content_setting_values.automatic_downloads': 1}
option.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=option)
# 设置打开的浏览器窗口最大化
driver.maximize_window()
# driver.set_page_load_timeout(30)
driver.get(url)

# 转到登录界面自动输入手机号密码进行登录
driver.find_element(By.XPATH, '//*[@id="loginLi"]/a').click()
text = driver.page_source
time.sleep(20)  # 等待页面渲染
# 进入iframe框
iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
driver.switch_to.frame(iframe)

# 下面的‘手机号’‘密码’输入自己中国裁判文书网注册的真实手机号密码
username = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/form/div/div[1]/div/div/div/input')
username.send_keys('17855107615')
time.sleep(2)

username = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/form/div/div[2]/div/div/div/input'
)
username.send_keys('Caoyihan7015!')
time.sleep(2)

captcha_image = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[1]/form/div/div[3]/div/div/div/img')
captcha_image.screenshot('captcha.png')
api_key = '8ef4d5850d970790349c9c78831adb21'
solver = TwoCaptcha(api_key)
text = solver.normal('captcha.png')
result = text['code']
username = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[1]/form/div/div[3]/div/div/div/input')
username.send_keys(result)
time.sleep(2)

driver.find_element(
    By.XPATH, '//*[@id="root"]/div[1]/form/div/div[4]/span').click()
time.sleep(3)

# 必须加上表单退出，否者就是死元素无法定位
driver.switch_to.default_content()

# 这行代码的作用就相当于你手动点了一下‘刑事案件’那个按钮
# 要下载民事案件就把下一行代码里的刑事案件改成‘民事案件’，以此类推
driver.find_element(By.LINK_TEXT, '刑事案件').click()

time.sleep(10)
# testHtml(driver.page_source)

_lastWindow = driver.window_handles[-1]
driver.switch_to.window(_lastWindow)

"""
按条件检索
"""
# 点击高级检索
driver.find_element(
    By.XPATH, '//*[@id="_view_1545034775000"]/div/div[1]/div[1]').click()
# 设置检索条件
# 地点
place = driver.find_element(By.XPATH, '//*[@id="s2"]')
place.send_keys('长丰县')
time.sleep(2)
# 程序
driver.find_element(By.XPATH, '//*[@id="s9"]').click()
driver.find_element(By.XPATH, '//*[@id="0201_anchor"]').click()
# time
time_begin = driver.find_element(By.XPATH, '//*[@id="cprqStart"]')
time_begin.send_keys('2019-01-01')
time_end = driver.find_element(By.XPATH, '//*[@id="cprqEnd"]')
time_end.send_keys('2019-12-31')

# 点击搜索按钮
driver.find_element(
    By.XPATH, '//*[@id="searchBtn"]').click()

# 将每页文件数设置为最大,15条
page_size_box = driver.find_element(
    By.XPATH, '//*[@id="_view_1545184311000"]/div[8]/div/select').click()
page = driver.find_element(
    By.XPATH, '//*[@id="_view_1545184311000"]/div[8]/div/select/option[3]').click()


def test_exceptions(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except:
        return False


# 转为dataframe,设置行标题
data = []
data = pd.DataFrame(
    data, columns=['标题', '案由', '案号', '法院', '裁判日期', '当事人', '案件正文'])

event_xpath = '//*[@id="_view_1545184311000"]/div[3]/div[2]/h4/a'
# if test_exceptions(event_xpath) == True:
driver.find_element(By.XPATH, event_xpath).click()
# 切换到新窗口
_lastWindow = driver.window_handles[-1]
driver.switch_to.window(_lastWindow)
driver.find_element(
    By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[1]/img').click()
# 保存制定内容
# 标题
title = driver.find_element(
    By.XPATH, '//*[@id="_view_1541573883000"]/div/div[1]/div[1]').text
# 案由
case_reason = driver.find_element(
    By.XPATH, '//*[@id="iframedf"]/span[1]').text
# 案号
case_number = driver.find_element(
    By.XPATH, '//*[@id="iframedfah"]/span[1]').text
# 法院
court = driver.find_element(
    By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[1]/a').text
# 裁判日期
judgment_date = driver.find_element(
    By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[5]/b').text
# 当事人
party = driver.find_element(
    By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[6]/b').text
# 案件正文
content = driver.find_element(
    By.XPATH, '//*[@id="2"]').text
data.loc[len(data)] = [title, case_reason, case_number, court,
                       judgment_date, party, content]

print(data)
# page = 1
# # 最多显示600条文件,也就是40页
# while page <= 40:
#     time.sleep(5+page/10)
#     for i in range(15):
#         time.sleep(5+i/10)
#         # 进入文书内部
#         event_xpath = '//*[@id="_view_1545184311000"]/div[' + \
#             str(i+3)+']/div[3]/div[2]/h4/a'
#         if test_exceptions(event_xpath) == True:
#             driver.find_element(By.XPATH, event_xpath).click()
#             # 切换到新窗口
#             _lastWindow = driver.window_handles[-1]
#             driver.switch_to.window(_lastWindow)
#             driver.find_element(
#                 By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[1]/img').click()
#             # 保存制定内容
#             # 标题
#             title = driver.find_element(
#                 By.XPATH, '//*[@id="_view_1541573883000"]/div/div[1]/div[1]').text
#             # 案由
#             case_reason = driver.find_element(
#                 By.XPATH, '//*[@id="iframedf"]/span[1]').text
#             # 案号
#             case_number = driver.find_element(
#                 By.XPATH, '//*[@id="iframedfah"]/span[1]').text
#             # 法院
#             court = driver.find_element(
#                 By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[1]/a').text
#             # 裁判日期
#             judgment_date = driver.find_element(
#                 By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[5]/b').text
#             # 当事人
#             party = driver.find_element(
#                 By.XPATH, '//*[@id="_view_1541573889000"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/h4[6]/b').text
#             # 案件正文
#             content = driver.find_element(
#                 By.XPATH, '//*[@id="2"]').text
#             data.loc[len(data)] = [title, case_reason, case_number, court,
#                                    judgment_date, party, content]
#             # 关闭当前窗口
#             driver.find_element(By.XPATH, '//*[@id="btnClose"]').click()
#         else:
#             event_xpath = '//*[@id="_view_1545184311000"]/div[' + \
#                 str(i+3) + ']/div[5]/div/a[2]'
#             if test_exceptions(event_xpath) == True:
#                 driver.find_element(By.XPATH, event_xpath).click()

#         # event_xpath = '//*[@id="_view_1545184311000"]/div[' + \
#         #     str(i+3) + ']/div[6]/div/a[2]'
#         # if test_exceptions(event_xpath) == True:
#         #     driver.find_element(By.XPATH, event_xpath).click()
#         # else:
#         #     event_xpath = '//*[@id="_view_1545184311000"]/div[' + \
#         #         str(i+3) + ']/div[5]/div/a[2]'
#         #     if test_exceptions(event_xpath) == True:
#         #         driver.find_element(By.XPATH, event_xpath).click()

#     # 下一页按钮,不能用Xpath定位,因为“下一页”按钮位置不固定
#     # driver.find_element(By.LINK_TEXT, '下一页').click()
#     time.sleep(5)
#     driver.find_element(By.LINK_TEXT, '下一页').click()
#     # 必须加上表单退出，否者就是死元素无法定位
#     driver.switch_to.default_content()
#     page += 1

# # # 关闭整个浏览器窗口并终止与浏览器的会话
# # driver.quit()
