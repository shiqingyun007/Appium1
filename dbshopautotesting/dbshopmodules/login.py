# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 16:33
# Software:PyCharm
# File:login.py


#登录界面，登录操作
import time

from selenium.webdriver.common.by import By


class Login:

    def __init__(self,driver):
        self.driver=driver

    def login(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/login_name').send_keys('jack')
        self.driver.find_element(By.ID,"com.insthub.ecmobile:id/login_password").send_keys('123456')
        self.driver.find_element(By.XPATH,"//android.widget.Button[@reso"
                                          "urce-id='com.insthub.ecmobile:id/login_login']").click()
        time.sleep(2)