# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 13:59
# Software:PyCharm
# File:back.py

import time

from selenium.webdriver.common.by import By

# 返回操作
class Back:
    def __init__(self,driver):
        self.driver=driver

    def backHomePage(self):
        while True:
            if self.driver.find_elements(By.ID,'com.insthub.ecmobile:id/toolbar_tabonebg')!=[]:#判断是否在主页
                break
            elif self.driver.find_elements(By.ID,'com.insthub.ecmobile:id/toolbar_tabone')!=[]:#判断是否有主页按钮
                self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabone').click()
            else:
                self.driver.press_keycode(4)#不在主页、也没有主页按钮，点击back返回上一个页面
            time.sleep(3)

    #返回1-n次
    def back(self,n):
        for i in range(n):
            self.driver.press_keycode(4)
            time.sleep(3)