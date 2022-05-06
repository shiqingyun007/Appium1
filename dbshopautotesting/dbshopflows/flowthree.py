# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-17 14:17
# Software:PyCharm
# File:flowthree.py

import random
import unittest
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage
from dbshopautotesting.dbshopmodules.search import Search
from dbshopautotesting.dbshopmodules.searchresult import SearchResult

# 备选流：
#       搜索模块相关操作：主页的手机类型、手机部件、充值卡、搜索按钮，
#       四部分随机向搜索结果页切换，切换至商品的详情页，再返回主页
class FlowThree(unittest.TestCase):
    def __init__(self,driver,action):
        super(FlowThree, self).__init__() # 使用assertEqual方法，需要在构造方法中调用父类的构造方法
        self.driver=driver
        self.action=action

    def flowThree(self):
        search=Search(self.driver,self.action)
        searchresult=SearchResult(self.driver,self.action)
        hp=HomePage(self.driver)
        # for i in range(10):
        #     HomePage().enterSearch(self.driver)  # 进入搜索模块
        #     search.randomEnter()
        #     BackHomePage.backHomePage(self.driver)# 返回主页
        for i in range(10):
            num=random.randint(1,4)
            if num==1:
                hp.search_phoneType()#进入手机类型搜索结果页
            elif num==2:
                hp.search_phonePart()#进入手机部件搜索结果页
            elif num==3:
                hp.search_refillCard()#进入充值卡搜索结果页
            else:
                hp.enterSearch()#进入搜索模块
                search.randomEnter()#进入搜索模块中随机选择类型，进入搜索结果页
            searchresult.resetSearchResult()#校验页面中是否有商品信息，没有重新选择类型
            searchresult.viewAllGoods()#遍历页面中的所有商品
            searchresult.randomEnterGoodDetail()#随机选择某商品进入其详情页面
            result=self.driver.find_element(By.XPATH,"//android.widget.TextView[@resource-id='com.insthub.ecmobile:id/top_view_text']").text
            self.assertEqual('商品详情',result)
            Back(self.driver).backHomePage()#返回主页