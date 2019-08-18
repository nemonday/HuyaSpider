import json
import time
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


class GetAnchorInfo(object):
    def __init__(self):
        self.opt = webdriver.ChromeOptions()
        # 随机请求头
        # self.opt.add_argument('user-agent="{}"'.format(choice(User_Agent_list)))
        # 无界面模式，需要看界操作，注释此行
        # self.opt.add_argument('--headless')
        # 部署服务器上 需要使用此两行代码
        # display = Display(visible=0, size=(800, 600))
        # display.start()

        # 添加代理
        proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=2&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        proxy = requests.get(proxy_url)
        proxy = json.loads(proxy.text)['data'][0]
        self.proxies = {
            'https': 'http://{0}:{1}'.format(proxy['ip'], proxy['port'])
        }
        self.opt.add_argument("--proxy-server={}".format(self.proxies['https']))

        self.prefs = {"profile.managed_default_content_settings.images": 2}
        self.opt.add_experimental_option("prefs", self.prefs)

        self.broser = webdriver.Chrome(options=self.opt)
        self.wait = WebDriverWait(self.broser, 20, 0.5)

        # 数据库位置
        self.engine = create_engine("mysql+pymysql://root:pythonman@127.0.0.1/proxy?charset=utf8")

        # 创建会话
        self.session = sessionmaker(self.engine)
        self.mySession = self.session()
        self.broser.maximize_window()

    def is_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.broser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as f:
            print('加载不出元素')
            pass

    def add_cookie(self):
        # 添加cookie
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147281.726353, 'httpOnly': False, 'name': 'h_unt', 'path': '/',
             'secure': False, 'value': '1563542499'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'httpOnly': False, 'name': '_yasids', 'path': '/', 'secure': False,
             'value': '__rootsid%3DC887317AFD200001F7D5B5E1160016DF'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'httpOnly': False, 'name': '__yaoldyyuid', 'path': '/', 'secure': False,
             'value': '1385441693'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105304, 'httpOnly': False, 'name': 'udb_status', 'path': '/',
             'secure': False, 'value': '0'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105268, 'httpOnly': False, 'name': 'udb_passport', 'path': '/',
             'secure': False, 'value': 'newqq__t7kmc1pz'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105192, 'httpOnly': False, 'name': 'udb_origin', 'path': '/',
             'secure': False, 'value': '100'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105155, 'httpOnly': False, 'name': 'udb_openid', 'path': '/',
             'secure': False, 'value': '24A21F4F2D99FD658319B2E0D9097932'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.10506, 'httpOnly': False, 'name': 'partner_uid', 'path': '/',
             'secure': False, 'value': '24A21F4F2D99FD658319B2E0D9097932'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105379, 'httpOnly': False, 'name': 'udb_version', 'path': '/',
             'secure': False, 'value': '1.0'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.10502, 'httpOnly': False, 'name': 'nickname', 'path': '/',
             'secure': False, 'value': 'Nemo'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1626614462, 'httpOnly': False, 'name': '__yamid_new', 'path': '/',
             'secure': False, 'value': 'C8873177E2800001ADCACFDE12001CA3'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105414, 'httpOnly': False, 'name': 'username', 'path': '/',
             'secure': False, 'value': 'newqq__t7kmc1pz'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.10496, 'httpOnly': False, 'name': 'avatar', 'path': '/',
             'secure': False, 'value': 'http://thirdqq.qlogo.cn/g?b=oidb&k=vFSfsKY22NHDcgGk4o5VUQ&s=100&t=1505179380'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1595078463, 'httpOnly': False, 'name': 'udb_guiddata', 'path': '/',
             'secure': False, 'value': '87b596b782504393ab1d2745758570b1'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'httpOnly': False, 'name': 'udb_passdata', 'path': '/', 'secure': False,
             'value': '3'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1625750480, 'httpOnly': False, 'name': 'smidV2', 'path': '/',
             'secure': False,
             'value': '20190719212103a3b0d66fc01f73c3fdf223e3525232f60094864735c6ea730'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'httpOnly': False, 'name': 'Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f', 'path': '/',
             'secure': False, 'value': '1563542481'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.10545, 'httpOnly': False, 'name': 'yyuid', 'path': '/',
             'secure': False, 'value': '1385441693'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'httpOnly': False, 'name': '__yasmid', 'path': '/', 'secure': False,
             'value': '0.8806154268684707'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105229, 'httpOnly': False, 'name': 'udb_other', 'path': '/',
             'secure': False, 'value': '%7B%22lt%22%3A%221563542491528%22%2C%22isRem%22%3A%221%22%7D'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1624022462, 'httpOnly': False, 'name': '__yamid_tt1', 'path': '/',
             'secure': False, 'value': '0.8806154268684707'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.421715, 'httpOnly': False, 'name': 'lType', 'path': '/',
             'secure': False, 'value': 'qq'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105101, 'httpOnly': False, 'name': 'udb_biztoken', 'path': '/',
             'secure': False,
             'value': 'AQCMv8Y9Tc13qhUjPdTfk3-tviFzGxVrTgnaJwYiDsFgeZXtuV8Qn9nNUx7tmCRLk-nJ4G-aDN66c_PD8fRiaH9Ge0iufy0P-_rx--KsLa_N23sZXwE9ulrEX_bFRrFqmpg_2cKTGVdEpyn_zJTBi9WHz06yZYZ_MQr30VBrCky4WGtgaSF-vFKYO_JrFOaiVbT63nw4qXylEmfpbuLC5tnDNGKAZ9RwPDaBeUuS3UQSCPLACiJUtVBBV4QbHQQjcgFHCMMzr9l4CFREpvOPX4FMAHq_opEDqty6e1Xo5gCLShziqFlSut2gh3tLjzK6J_rMVw9i_dNWp0BMugvsuKec'})
        self.broser.add_cookie({'domain': '.huya.com', 'expiry': 1595078481, 'httpOnly': False,
                                'name': 'Hm_lvt_51700b6c722f5bb4cf39906a596ea41f', 'path': '/', 'secure': False,
                                'value': '1563542461'})
        self.broser.add_cookie(
            {'domain': '.huya.com', 'expiry': 1564147274.105338, 'httpOnly': False, 'name': 'udb_uid', 'path': '/',
             'secure': False, 'value': '1385441693'})
        self.broser.add_cookie(
            {'domain': 'www.huya.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False,
             'value': 'j7u4h4vv1m0m3hu433ul3o64g3'})

    def run(self):
        # 查询结果集
        results = self.mySession.query(Type).all()
        for result in results:
            type_id = result.id
            type = result.type
            type_url = result.type_url
            self.broser.get(type_url)

            self.add_cookie()

            url_list = []
            self.is_visible('//*[@id="js-live-list"]/li')
            anchor_info_lists = self.broser.find_elements_by_xpath('//*[@id="js-live-list"]/li')
            for anchor_info in anchor_info_lists:
                anchor_url = anchor_info.find_element_by_xpath('.//a[@class="video-info new-clickstat "]').get_attribute('href')
                url_list.append(anchor_url)

            for url in url_list:
                self.broser.get(url)
                # 主播名字
                anchor_name = self.broser.find_element_by_xpath('//*[@id="J_roomHeader"]/div[1]/div[2]/div[2]/h3').text
                # 主播粉丝数
                follow = self.broser.find_element_by_xpath('//*[@id="activityCount"]').text
                # 主播id
                anchor_id = self.broser.find_element_by_xpath('//*[@id="J_roomHeader"]/div[1]/div[2]/div[2]/span[3]/em').text
                try:
                    info = Anchor(anchor_type_id=type_id, anchor_type=type, anchor_name=anchor_name, anchor_id=anchor_id, anchor_follow=follow, anchor_url=url)
                    self.mySession.add(info)
                    self.mySession.commit()
                    fans_dict = {}

                    self.is_visible('//*[@id="J_weekRankList"]/li[1]/span[3]')
                    ele = self.broser.find_element_by_xpath('//*[@id="J_weekRankList"]/li[1]/span[3]')
                    ActionChains(self.broser).move_to_element(ele).perform()
                    fans = self.broser.find_elements_by_xpath('//*[@id="J_weekRankList"]/li')

                    for i in range(20):
                        for fan in fans:
                            try:
                                fan_name = fan.find_element_by_xpath('.//span[@class="week-rank-name J_name"]').text
                                fan_price = fan.find_element_by_xpath('.//span[@class="gold-num"]').text
                                fans_dict[fan_name] = fan_price
                            except:
                                pass

                        Drag = self.broser.find_element_by_class_name('jspDrag')  # 找到滚动条
                        # 控制滚动条的行为，每次向y轴(及向下)移动10个单位
                        ActionChains(self.broser).drag_and_drop_by_offset(Drag, 0, 15).perform()
                        time.sleep(1)  # 休眠2秒
                        fans = self.broser.find_elements_by_xpath('//*[@id="J_weekRankList"]/li')

                    for fan_name, pirce in fans_dict.items():
                        if fan_name and pirce is not None:
                            # 赠送的的礼物值
                            pirce = int(pirce.replace(',', ''))
                            # 折合人名币
                            rmb = pirce / 1000
                            info = Fans(fan_follow_id=anchor_id, fan_name=fan_name.encode('utf-8'), fan_pirce=pirce, rmb=rmb)
                            self.mySession.add(info)
                            self.mySession.commit()

                    self.broser.back()

                except Exception as f:
                    print(f)
                    self.broser.back()

            try:
                # 翻页操作
                click_element = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="laypage_next"]')))
                ActionChains(self.broser).move_to_element(click_element).click().perform()
            except:
                pass

        self.broser.quit()


if __name__ == '__main__':
    obj = GetAnchorInfo()
    obj.run()