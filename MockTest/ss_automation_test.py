#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '192.168.1.104:5555'
        desired_caps['appPackage'] = 'com.github.shadowsocks'
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("setUp")

    @data(("test", "test", "8888")
          )

    @unpack
    def testSeupVPN(self, ip, password, port):
        self.driver.find_elements_by_class_name("android.widget.TextView")[1].click()  # 点击+图标
        self.driver.find_elements_by_class_name("android.widget.TextView")[2].click()  # 点击Mannual Setting
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()

        print("start inputing ip address")
        # 输入ip地址
        self.driver.find_element_by_id("edit").clear()
        self.driver.find_element_by_id("edit").send_keys("207.246.112.167")
        self.driver.find_element_by_id("button1").click()

        # 输入密码
        print("start inputing password")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[4].click()
        self.driver.find_element_by_id("edit").clear()
        self.driver.find_element_by_id("edit").send_keys("0m&TM^G!Bo16Sm@JkSD!VgxO7Iz%Sb@Hi@uu8Jo0wt%M6S@XY6*&YP")
        self.driver.find_element_by_id("button1").click()

        print("start inputing encryption method")
        # 选择加密方式
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[5].click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[contains(@text,"CHACHA20")]').click()

        print("start inputing port")
        # 查找端口号
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[2].click()
        self.driver.find_element_by_id("numberpicker_input").click()
        self.driver.find_element_by_id("numberpicker_input").clear()
        self.driver.find_element_by_id("numberpicker_input").send_keys("4593")
        self.driver.find_element_by_id("button1").click()

        print("start pressing OK to get back main screen")
        #点击确定回到主界面
        textviews=self.driver.find_elements_by_class_name("android.widget.TextView")
        print(textviews)
        action_apply = self.driver.find_element_by_id("action_apply")
        print(action_apply)
        self.driver.find_element_by_id("action_apply").click()


    def tearDown(self):
        print("quit")
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)