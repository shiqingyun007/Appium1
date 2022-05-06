# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 10:02
# Software:PyCharm
# File:addAddress.py
import time
from selenium.webdriver.common.by import By

class ShippingAddress:

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action
    # 添加收货地址
    def addAddressInfo(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/add_address_name').send_keys('jack')
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/add_address_telNum').send_keys('123456')
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/add_address_zipCode').send_keys('123456')
        self.action.tap(None,300,460).wait(3000).tap(None,80,700).wait(3000).tap(None,80,230).wait(3000).\
            tap(None,80,700).wait(3000).tap(None,100,200).wait(3000).perform()
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/add_address_detail').send_keys('拱墅区110号')
        self.action.tap(None,350,650).perform()
        time.sleep(3)
