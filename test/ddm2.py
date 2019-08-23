import json
from random import choice
import time
import requests
from selenium import webdriver
import schedule


def Adfly():
    url = 'https://proxy.horocn.com/api/proxies?order_id=DXSN1642674010105319&num=3&format=json&line_separator=win&can_repeat=no'
    rsp = requests.get(url)
    proxys = json.loads(rsp.text)

    for proxy in proxys:
        host = proxy['host']
        port = proxy['port']
        opt = webdriver.ChromeOptions()
        PC_USER_ANGENT_LIST = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            # 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            # 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            # 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            # 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        ]
        # 随机请求头
        user_angent = choice(PC_USER_ANGENT_LIST)
        opt.add_argument('user-agent=%s'% user_angent)
        # proxys = '--proxy-server=http://{}:{}'.format(host, port)
        # opt.add_argument(proxys)
        # opt.add_argument('Proxy-Authorization={}'.format(auth))
        # opt.add_argument('--proxy-server=http://forward.xdaili.cn:80')
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # opt.add_experimental_option("prefs", prefs)
        # opt.add_argument('--headless')

        try:
            broser = webdriver.Chrome(options=opt)
            broser.set_script_timeout(3)
            url = 'http://festyy.com/w3I1PT'
            broser.delete_all_cookies()
            broser.get(url)
            time.sleep(1)
            broser.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
            print('is ok')
            broser.quit()
        except Exception as f:
            broser.quit()



while True:
    Adfly()