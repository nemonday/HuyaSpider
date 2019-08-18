from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
client = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path='/root/ddm/test/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径

client.get("https://www.baidu.com")
print(client.page_source.encode('utf-8'))

client.quit()
