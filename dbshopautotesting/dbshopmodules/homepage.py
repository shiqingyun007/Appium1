# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 14:06
# Software:PyCharm
# File:homepage.py
import random
import time
from selenium.webdriver.common.by import By

#dbshop主界面相关操作
class HomePage:

    def __init__(self,driver):
        self.driver=driver

    # 进入 飞利浦9@9v手机 商品详情页
    def philips(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/good_cell_photo_three').click()
        time.sleep(3)

    # 进入  KD876 商品详情页
    def KD876(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/good_cell_photo_two').click()
        time.sleep(3)

    # 进入手机类型-搜索结果页
    def search_phoneType(self):
        self.driver.tap([(200,500)],1)
        time.sleep(3)

    # 进入手机配件-搜索结果页
    def search_phonePart(self):
        self.driver.tap([(200,800)],1)
        time.sleep(3)

    # 进入充值卡-搜索结果页
    def search_refillCard(self):
        self.driver.tap([(200,1100)],1)
        time.sleep(3)

    # 进入  移动20元充值卡 商品详情页
    def refileCard20(self):
        self.driver.tap([(600,1000)],1)
        time.sleep(3)

    # 进入  小灵通/固话50元充值卡  商品详情页
    def refileCard50(self):
        self.driver.tap([(600,1150)],1)
        time.sleep(3)

    # 进入 搜索模块
    def enterSearch(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo').click()
        time.sleep(3)

    # 进入 购物车模块
    def enterGoodsCart(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabthree').click()
        time.sleep(3)

    # 进入 个人中心模块
    def enterPersonalCenter(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabfour').click()
        time.sleep(3)

    #随机进入某个商品的详情页面
    def randomEnterGD(self):
        num = random.randint(1, 4)
        if num == 1:
            self.philips()
        elif num == 2:
            self.KD876()
        elif num == 3:
            self.refileCard20()
        else:
            self.refileCard50()