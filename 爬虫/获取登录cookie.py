import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Edge()

try:
    # 打开小红书主页并手动登录
    driver.get("https://www.dhsprogram.com/data/dataset_admin/login_main.cfm")
    time.sleep(40)  # 给用户足够的时间手动登录

    # 获取登录后的 cookie
    cookies = driver.get_cookies()

    # 打印当前工作目录
    print("Current working directory: ", os.getcwd())

    # 将 cookie 保存到文件
    with open("cookies.json", "w") as file:
        json.dump(cookies, file)
    print("Cookies saved successfully.")
finally:
    driver.quit()
