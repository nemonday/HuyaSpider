import json
import time

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
    chrome_options.add_argument("--proxy-server={}".format(proxies['https']))
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
    client = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='/root/ddm/test/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径

    for i in range(3):
        urls2 = 'http://dd.ma/4XmpxwTg'
        client.delete_all_cookies()
        client.get(urls2)
        time.sleep(5)
        client.find_element_by_xpath('//*[@id="btn_open"]/a').click()
        print('点击')
        time.sleep(1)

    client.quit()


while True:
    ddm()
