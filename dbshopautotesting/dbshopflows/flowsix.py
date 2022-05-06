# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-24 14:33
# Software:PyCharm
# File:flowsix.py
import unittest

from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.close_account import CloseAccount
from dbshopautotesting.dbshopmodules.goodscart import GoodsCart
from dbshopautotesting.dbshopmodules.goodsdetails import GoodDetail
from dbshopautotesting.dbshopmodules.homepage import HomePage



# 流程6：主页-》商品详情-》购物车-》结算
from dbshopautotesting.dbshopmodules.welcomepage import WelcomePage


class FlowSix(unittest.TestCase):

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    def flowSix(self):
        hp=HomePage(self.driver)
        gd=GoodDetail(self.driver,self.action)
        gc=GoodsCart(self.driver,self.action)
        ca=CloseAccount(self.driver,self.action)
        back=Back(self.driver)

        # 欢迎界面相关操作
        WelcomePage(self.driver).fiveSwipe()

        # 由主页随机进入商品详情页面
        hp.randomEnterGD()

        # 商品详情页相关操作
        gd.viewImage() # 查看图片
        gd.modifyGood() # 修改商品数量
        gd.viewGoodsMessage() # 查看商品相关信息
        gd.addFavorites()
        gd.addShopCart() # 商品加入购物车
        gd.enterGoodsCart() # 进入购物车
        back.back(1)
        gd.buy() # 点击立即购买，进入购物车

        # 购物车相关操作
        gc.modify_goodsNum() # 修改商品数量
        gc.buttonCloseAccount() # 结算

        # 结算相关操作
        ca.closeAccount()

        #返回首页
        back.backHomePage()