# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-17 14:35
# Software:PyCharm
# File:search.py
import random
import time

from selenium.webdriver.common.by import By

from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage


class Search:

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    #进入搜索模块，随机进入手机类型、手机配件、充值卡模块
    def randomEnter(self):
        num=random.randint(1,3)
        if num==1:
            self.phoneType()
        elif num==2:
            self.phonePart()
        else:
            self.refillCard()
    # 进入搜索二级目录：手机类型
    def enterPhoneType(self):
        self.driver.tap([(70, 160)], 1)
        time.sleep(3)

    # 手机类型相关操作
    def phoneType(self):
        self.enterPhoneType()
        num = random.randint(1, 4)
        #手机类型中：随机进入CDMA手机、GSM手机、3G手机、双模手机
        if num == 1:
            self.driver.tap([(70,150)],1)
        elif num == 2:
            self.driver.tap([(70,250)],1)
        elif num == 3:
            self.driver.tap([(70,350)],1)
        else:
            self.driver.tap([(70,450)],1)
        time.sleep(3)

    # 进入搜索二级目录：手机配件
    def enterPhonePart(self):
        self.driver.tap([(70, 250)], 1)
        time.sleep(3)

    # 手机配件相关操作
    def phonePart(self):
        self.enterPhonePart()
        num = random.randint(1, 4)
        # 手机类型中：随机进入充电器、耳机、电池、读卡器和内存
        if num == 1:
            self.driver.tap([(70, 150)], 1)
        elif num == 2:
            self.driver.tap([(70, 250)], 1)
        elif num == 3:
            self.driver.tap([(70, 350)], 1)
        else:
            self.driver.tap([(70, 450)], 1)
        time.sleep(3)

    # 进入搜索二级目录：充值卡
    def enterRefillCard(self):
        self.driver.tap([(70, 330)], 1)
        time.sleep(3)

    # 充值卡相关操作
    def refillCard(self):
        self.enterRefillCard()
        num = random.randint(1, 3)
        # 手机类型中：随机进入小灵通固话充值卡、移动手机充值卡、联通手机充值卡
        if num == 1:
            self.driver.tap([(70, 150)], 1)
        elif num == 2:
            self.driver.tap([(70, 250)], 1)
        else:
            self.driver.tap([(70, 350)], 1)
        time.sleep(3)

    # 进入购物车
    def enterGoodsCart(self):
        #判断是否在搜索模块的一级目录
        if self.driver.find_elements(By.XPATH,"//android.widget.TextView[@resource-id='com.insthub."
                                              "ecmobile:id/category_name' and @text='手机类型']")!=[]:
            self.driver.find_element(By.ID,'com.insthub.ecmobile:id/toolbar_tabthree').click()
        else:
            self.driver.press_keycode(4)#二级目录需要先返回一级目录，再点击购物车按钮
            time.sleep(3)
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabthree').click()
        time.sleep(3)

    # 进入个人中心
    def enterPersonalCenter(self):
        #判断是否在搜索模块的一级目录
        if self.driver.find_elements(By.XPATH,"//android.widget.TextView[@resource-id='com.insthub."
                                              "ecmobile:id/category_name' and @text='手机类型']")!=[]:
            self.driver.find_element(By.ID,'com.insthub.ecmobile:id/toolbar_tabfour').click()
        else:
            self.driver.press_keycode(4)#二级目录需要先返回一级目录，再点击个人中心
            time.sleep(3)
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabfour').click()
        time.sleep(3)