import json
import time
from random import choice

import requests
from selenium import webdriver


def Adfly():
    url = 'https://proxy.horocn.com/api/proxies?order_id=DXSN1642674010105319&num=3&format=json&line_separator=win&can_repeat=no'
    rsp = requests.get(url)
    proxys = json.loads(rsp.text)

    for proxy in proxys:
        host = proxy['host']
        port = proxy['port']

        chrome_options = webdriver.ChromeOptions()
        PC_USER_ANGENT_LIST = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            # 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
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
        # chrome_options.add_argument('user-agent="%s"' % user_angent)
        proxys = '--proxy-server=http://{}:{}'.format(host, port)
        chrome_options.add_argument("{}".format(proxys))

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
        client = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='/root/ddm/test/chromedriver'
                                  )  # 如果没有把chromedriver加入到PATH中，就需要指明路径

        client.set_page_load_timeout(5)  # 5秒

        try:
            url = 'http://tenteaea.com/1SdB'
            client.delete_all_cookies()
            client.get(url)
            time.sleep(1)
            client.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
            print('点击:{}'.format(url))
            client.quit()
        except:
            # client.execute_script('window.stop()')      # 执行Javascript来停止页面加载 window.stop()
            client.quit()

while True:
    Adfly()