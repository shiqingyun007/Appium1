# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 10:31
# Software:PyCharm
# File:initialize.py
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


# 结算提交订单，返回配送方式
class CloseAccount():

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    def closeAccount(self):
        #支付方式选择货到付款，配送方式选择城际快递
        self.action.tap(None,400,350).wait(3000).tap(None,400,180).wait(3000).\
            tap(None,400,400).wait(3000).tap(None,400,250).wait(2000).perform()

        # 点击提交订单
        self.action.tap(None,600,1050).wait(3000).perform()