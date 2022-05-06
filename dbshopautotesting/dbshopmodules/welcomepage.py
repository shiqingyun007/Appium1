# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 15:02
# Software:PyCharm
# File:welcomepage.py
import time

from selenium.webdriver.common.by import By


class WelcomePage:

    def __init__(self,driver):
        self.driver=driver

    # 向左滑屏5次
    def fiveSwipe(self):
        time.sleep(3)
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabfour') == []:
            for i in range(5):
                self.driver.swipe(700, 640, 200, 640)  # 滑屏，跳过欢迎界面
                time.sleep(1)
            time.sleep(2)