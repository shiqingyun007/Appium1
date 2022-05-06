# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-19 13:03
# Software:PyCharm
# File:flowfour.py

import random
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage
from dbshopautotesting.dbshopmodules.search import Search
from dbshopautotesting.dbshopmodules.searchresult import SearchResult

# 搜索结果页相关操作
class FlowFour:
    def __init__(self,driver,action):
        super(FlowFour,self).__init__()
        self.driver=driver
        self.action=action

    def flowFour(self):
        sr=SearchResult(self.driver,self.action)
        hp=HomePage(self.driver)
        search=Search(self.driver,self.action)
        back=Back(self.driver)

        #随机通过不同方式进入搜索结果页
        num = random.randint(1, 4)
        if num == 1:
            hp.search_phoneType()  # 进入手机类型搜索结果页
        elif num == 2:
            hp.search_phonePart()  # 进入手机部件搜索结果页
        elif num == 3:
            hp.search_refillCard()  # 进入充值卡搜索结果页
        else:
            hp.enterSearch()  # 进入搜索模块
            search.randomEnter()  # 进入搜索模块中随机选择类型，进入搜索结果页

        sr.resetSearchResult()#检查页面是否有商品，没有商品返回重新操作
        sr.loadGoods()#加载出页面的所有商品
        sr.changeSort()#切换排序为人气排行
        sr.selectConfig()#配置筛选
        sr.viewAllGoods()#查看所有商品
        sr.randomEnterGoodDetail()#随机选择一个商品进入其详情页面
        back.back(1)#返回1次
        sr.enterGoodsCart()#进入购物车
        back.backHomePage()#返回主页