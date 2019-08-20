import json
import time
from multiprocessing import Process
from random import choice
from threading import Thread

import pymysql
import requests
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait





def Adfly():
    url = 'http://ged.ip3366.net/api/?key=20190820084107625&getnum=1&isp=1&anonymoustype=3&filter=1&area=1&order=1'
    rsp = requests.get(url)

    opt = webdriver.ChromeOptions()
    PC_USER_ANGENT_LIST = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        # 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        # 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        # 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    ]
    # 随机请求头
    user_angent = choice(PC_USER_ANGENT_LIST)
    opt.add_argument('user-agent="%s"'% user_angent)



    try:
        # opt.add_argument('--headless')
        opt.add_argument("--proxy-server=http://{}".format(rsp.text))

        # prefs = {"profile.managed_default_content_settings.images": 2}
        # opt.add_experimental_option("prefs", prefs)
        broser = webdriver.Chrome(options=opt)
        broser.set_script_timeout(10)

        wait = WebDriverWait(broser, 20, 0.5)

        urls_list = ['http://dd.ma/yMexDitA',
                     'http://dd.ma/bSEokjKq'
                     ]
        url = choice(urls_list)
        broser.delete_all_cookies()
        broser.get(url)
        time.sleep(1)
        broser.find_element_by_xpath('//*[@id="btn_open"]/a').click()
        print('点击 {}'.format(url))
        broser.quit()
    except:
        time.sleep(3)
        broser.quit()

#



while True:
    Adfly()
