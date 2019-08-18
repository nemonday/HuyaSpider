import json
import time
from multiprocessing import Process
from random import choice
from threading import Thread

import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import create_engine
from Model import Type, Anchor, Fans
from sqlalchemy.orm import sessionmaker
from selenium.webdriver.common.action_chains import ActionChains

from Parameter import PC_USER_ANGENT_LIST




def Adfly():
    opt = webdriver.ChromeOptions()
    # 随机请求头
    user_angent = choice(PC_USER_ANGENT_LIST)
    # opt.add_argument('user-agent="%s"'% user_angent)
    # 无界面模式，需要看界操作，注释此行
    # opt.add_argument('--headless')
    # 部署服务器上 需要使用此两行代码
    # display = Display(visible=0, size=(800, 600))
    # display.start()


    try:
        opt.add_argument('--headless')
        proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=2&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        proxy = requests.get(proxy_url)
        print(proxy.text)
        proxy = json.loads(proxy.text)['data'][0]
        proxies = {
            'https': 'http://{0}:{1}'.format(proxy['ip'], proxy['port'])
        }
        opt.add_argument("--proxy-server={}".format(proxies['https']))
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # opt.add_experimental_option("prefs", prefs)
        broser = webdriver.Chrome(options=opt)
        wait = WebDriverWait(broser, 20, 0.5)
        broser.maximize_window()

        for i in range(3):
            urls2 = 'http://dd.ma/4XmpxwTg'
            broser.delete_all_cookies()
            broser.get(urls2)
            time.sleep(5)
            broser.find_element_by_xpath('//*[@id="btn_open"]/a').click()
            print('点击')
            time.sleep(1)
        broser.quit()
    except:
        broser.quit()

#



while True:
    Adfly()
