import time

from selenium import webdriver

def ddm():
    chrome_options = webdriver.ChromeOptions()
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
