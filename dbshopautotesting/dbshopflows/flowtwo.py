# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 17:12
# Software:PyCharm
# File:flowtwo.py

import unittest
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.goodsdetails import GoodDetail
from dbshopautotesting.dbshopmodules.homepage import HomePage

#购物车相关操作：从主界面->商品详情页->添加购物车（未登录，需要登录）->立即购买，进入购物车->返回上一页
class FlowTwo(unittest.TestCase):
    def __init__(self,driver,action):
        super(FlowTwo, self).__init__()
        self.driver=driver
        self.action=action

    def flowTwo(self):
        hp=HomePage(self.driver)
        gd=GoodDetail(self.driver,self.action)
        hp.randomEnterGD()# 随机进入首页的某个商品详情页中
        gd.addShopCart()#商品添加购物车
        gd.buy()#点击立即购买，进入购物车
        self.driver.press_keycode(4)#返回商品详情
        gd.viewImage()#查看商品图片
        gd.modifyGood()#修改商品数量
        gd.viewGoodsMessage()#查看商品基本信息
        gd.addFavorites()#加入收藏
        gd.enterGoodsCart()#进入购物车
        result=self.driver.find_element(By.XPATH,"//android.widget.TextView[@text='购物车']").text
        self.assertEqual('购物车',result)
        Back(self.driver).backHomePage()#返回主界面