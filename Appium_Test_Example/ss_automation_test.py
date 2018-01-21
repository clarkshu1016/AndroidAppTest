# usr/bin/python
# encoding:utf-8
import time

import os

from appium import webdriver
import unittest

from appium.webdriver.common.touch_action import TouchAction
from ddt import ddt, data, unpack

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@ddt
class MyTestCase(unittest.TestCase):
    # def setUp(self):
    #     desired_caps = {}
    #     desired_caps['autoGrantPermissions'] = 'true'
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '7.1.2'
    #     desired_caps['deviceName'] = '192.168.1.104:5555'
    #     desired_caps['appPackage'] = 'com.github.shadowsocks'
    #     desired_caps['appActivity'] = '.MainActivity'
    #     desired_caps["unicodeKeyboard"] = "True"
    #     desired_caps["resetKeyboard"] = "True"
    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #     print("setUp")
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'shadowsocks-nightly-4.4.0.apk'
        )
        desired_caps['appPackage'] = 'com.github.shadowsocks'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("test", "8888", "test", "AES-256-CFB"))
    @unpack
    def testSeupVPN(self, ip, port, password, encryption_method):
        action = TouchAction(self.driver)
        # set up array of two coordinates
        positions = []
        positions.append((100, 200))
        time.sleep(1)
        positions.append((100, 400))
        time.sleep(1)
        positions.append((500, 199))
        positions.append((500, 199))

        self.driver.tap(positions)

        # self.driver.find_elements_by_class_name("android.widget.TextView")[1].click()  # 点击+图标
        # self.driver.find_elements_by_class_name("android.widget.TextView")[2].click()  # 点击Mannual Setting
        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
        #
        # print("输入ip地址")
        # self.driver.find_element_by_id("edit").clear()
        # self.driver.find_element_by_id("edit").send_keys(ip)
        # self.driver.find_element_by_id("button1").click()
        #
        # print("输入端口号")
        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[2].click()
        # # self.driver.find_element_by_xpath('//android.widget.EditText[contains(@text,"8388")]').clear().send_keys(port)
        # self.driver.find_element_by_id("edit").clear()
        # self.driver.find_element_by_id("edit").send_keys(port)
        # self.driver.find_element_by_id("button1").click()
        #
        # print("输入密码")
        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[4].click()
        # self.driver.find_element_by_id("edit").clear()
        # self.driver.find_element_by_id("edit").send_keys(password)
        # self.driver.find_element_by_id("button1").click()
        #
        # print("选择加密方式")
        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[5].click()
        # self.driver.find_element_by_class_name("android.support.v7.widget.RecyclerView")
        # self.driver.find_element_by_xpath('//android.widget.CheckedTextView[contains(@text,'+encryption_method+')]').click()
        #
        #
        #
        # print("回退到shadowsocks 主界面")
        # #点击确定回到主界面
        # textviews=self.driver.find_elements_by_class_name("android.widget.TextView")
        # print(textviews)
        # action_apply = self.driver.find_element_by_id("action_apply")
        # print(action_apply)
        # self.driver.find_element_by_id("action_apply").click()

    def tearDown(self):
        print("quit")
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase).run()
