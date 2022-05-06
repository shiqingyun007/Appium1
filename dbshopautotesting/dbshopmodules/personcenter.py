# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-22 14:34
# Software:PyCharm
# File:personcenter.py

import time
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.login import Login

class PersonCenter:
    def __init__(self,driver):
        self.driver=driver

    # @classmethod
    # def a(cls):#通过  类名.方法名()   调用    普通方法的调用：构造方法().方法名()
    #     pass
    def isLogin(self):
        if self.driver.find_element(By.ID,'com.insthub.ecmobile:id/profile_head_name').text=='点击此处登录':
            self.driver.find_element(By.ID,'com.insthub.ecmobile:id/profile_head_name').click()
            time.sleep(3)
            Login(self.driver).login()

    def enterSearch(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo').click()
        time.sleep(3)