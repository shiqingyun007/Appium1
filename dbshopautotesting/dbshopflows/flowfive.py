# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-19 23:02
# Software:PyCharm
# File:flowfive.py
import random

from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage
from dbshopautotesting.dbshopmodules.search import Search


class FlowFive:
    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    def flowFive(self):
        hp=HomePage(self.driver)
        search=Search(self.driver,self.action)
        back=Back(self.driver)
        for i in range(5):
            hp.enterSearch()#进入搜索模块
            search.enterGoodsCart()#进入购物车
            back.backHomePage()#返回主页

            hp.enterSearch()#进入搜索模块
            num=random.randint(1,3)
            if num==1:
                search.enterPhoneType()#进入搜索二级目录->手机类型
            elif num==2:
                search.enterPhonePart()#进入搜索二级目录->手机配件
            else:
                search.enterRefillCard()#进入搜索二级目录->充值卡
            search.enterGoodsCart()#进入购物车
            back.backHomePage()
        for i in range(5):
            hp.enterSearch()#进入搜索模块
            search.enterPersonalCenter()#进入个人中心
            back.backHomePage()#返回主页

            hp.enterSearch()#进入搜索模块
            num=random.randint(1,3)
            if num==1:
                search.enterPhoneType()#进入搜索二级目录->手机类型
            elif num==2:
                search.enterPhonePart()#进入搜索二级目录->手机配件
            else:
                search.enterRefillCard()#进入搜索二级目录->充值卡
            search.enterPersonalCenter()#进入个人中心
            back.backHomePage()
