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
    opt = webdriver.ChromeOptions()
    PC_USER_ANGENT_LIST = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        # 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    ]
    # 随机请求头
    user_angent = choice(PC_USER_ANGENT_LIST)
    opt.add_argument('user-agent="%s"'% user_angent)
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
            urls_list = ['http://dd.ma/H1hI4jvk',
                         'http://dd.ma/hUupP4Fv',
                         'http://dd.ma/RaUZ7hEr',
                         'http://dd.ma/YRhBeubE',
                         'http://dd.ma/wGX6tAah',
                         'http://dd.ma/I7GLAjda',
                         ]

            url = choice(urls_list)
            broser.delete_all_cookies()
            broser.get(url)
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
