import json
import time
from random import choice

import requests
from selenium import webdriver


def ddm():
    chrome_options = webdriver.ChromeOptions()
    proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=2&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    proxy = requests.get(proxy_url)
    print(proxy.text)
    proxy = json.loads(proxy.text)['data'][0]
    proxies = {
        'https': 'http://{0}:{1}'.format(proxy['ip'], proxy['port'])
    }
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
    chrome_options.add_argument('user-agent="%s"' % user_angent)
    chrome_options.add_argument("--proxy-server={}".format(proxies['https']))
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
    client = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='/root/ddm/test/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径

    for i in range(3):
        urls2 = 'http://dd.ma/GbSfLvyK'
        client.delete_all_cookies()
        client.get(urls2)
        time.sleep(5)
        client.find_element_by_xpath('//*[@id="btn_open"]/a').click()
        print('点击')
        time.sleep(1)

    client.quit()


while True:
    ddm()
