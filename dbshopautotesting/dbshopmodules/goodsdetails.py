# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 16:29
# Software:PyCharm
# File:goodsdetails.py
import time
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.login import Login

# 商品详情页相关操作
class GoodDetail:

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action
        self.login=Login(self.driver)
    #获取库存
    def getInventory(self):
        time.sleep(3)
        # 获取商品的属性信息
        str = self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/good_property').text
        time.sleep(3)
        # 在字符串中截取出 库存数量
        lis1 = str.split()
        lis2 = lis1[1].split('：')
        self.__inventory = int(lis2[1])
        return self.__inventory

    # 商品添加至购物车
    def addShopCart(self):
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.in"
                                           "sthub.ecmobile:id/add_to_cart']").click()
        time.sleep(2)

        # 判断是否登录
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/login_name') != []:
            self.login.login()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.in"
                                               "sthub.ecmobile:id/add_to_cart']").click()
            time.sleep(2)

        # 判断是否有商品款式颜色等选项，有->点击确定
        if self.driver.find_elements(By.ID,'com.insthub.ecmobile:id/shop_car_item_ok')!=[]:
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/shop_car_item_ok').click()
            time.sleep(2)

    # 商品详情页，立即购买
    def buy(self):
        #判断库存的数量是否大于等于1，满足条件点击立即购买
        if self.getInventory()>=1:
            self.driver.tap([(200, 1250)], 1)
            time.sleep(3)
        #判断是否登录
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/login_name') != []:
            self.login.login()
            time.sleep(3)
            #点击立即购买，跳转至购物车页面
            self.driver.tap([(200, 1250)], 1)
            time.sleep(3)

    # 查看商品图片，并进行滑动
    def viewImage(self):
        self.driver.tap([(200,350)],1)
        time.sleep(3)
        for i in range(3):#左滑3次
            self.driver.swipe(700,640,200,640)
            time.sleep(2)
        for i in range(3):#右滑3次
            self.driver.swipe(200, 640, 700, 640)
            time.sleep(2)
        self.action.tap(None,360,640).wait(100).tap(None,360,640).wait(2000).perform()#双击放大图片
        self.driver.press_keycode(4)#返回商品详情
        time.sleep(3)

    # 修改商品数量、颜色款式
    def modifyGood(self):
        if self.getInventory()>1:#判断库存是否大于1com.insthub.ecmobile:id/shop_car_item_sum
            self.action.tap(None,300,700).wait(3000).tap(None,430,500).wait(1000).tap(None,430,650)\
                .wait(3000).tap(None,400,820).wait(3000).perform()

    # 查看商品的基本参数、商品评论、商品描述
    def viewGoodsMessage(self):
        self.action.tap(None,400,820).wait(2000).tap(None,50,80).wait(3000).perform()#基本参数
        self.action.tap(None, 400, 900).wait(2000).tap(None, 50, 80).wait(3000).perform()#商品描述
        self.action.tap(None, 400, 960).wait(2000).tap(None, 50, 80).wait(3000).perform()#商品评论

    # 将商品加入收藏
    def addFavorites(self):
        self.action.tap(None,60,1245).wait(3000).perform()#点击收藏
        # 判断是否登录
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/login_name') != []:
            self.login.login()
            time.sleep(2)
            self.action.tap(None, 60, 1245).wait(3000).perform()  # 点击收藏

    # 通过购物车按钮进入购物车
    def enterGoodsCart(self):
        self.action.tap(None, 650, 1250).wait(3000).perform()
        # 判断是否登录
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/login_name') != []:
            self.login.login()
            time.sleep(3)
        # 点击立即购买，跳转至购物车页面
        self.action.tap(None, 650, 1250).wait(3000).perform()