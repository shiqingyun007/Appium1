# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 16:06
# Software:PyCharm
# File:flowone.py
import unittest
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage

#流程1：主页向其他页面切换,最后返回主界面
class FlowOne(unittest.TestCase):

    def __init__(self,driver):
        super(FlowOne, self).__init__()
        self.driver=driver

    def flowOne(self):
        hp = HomePage(self.driver)
        bp=Back(self.driver)

        hp.KD876()
        bp.backHomePage()

        hp.philips()
        bp.backHomePage()
    
        hp.search_phoneType()
        bp.backHomePage()
    
        hp.search_phonePart()
        bp.backHomePage()
    
        hp.search_refillCard()
        bp.backHomePage()

        hp.randomEnterGD()
        bp.backHomePage()
    
        hp.enterSearch()
        bp.backHomePage()
    
        hp.enterGoodsCart()
        bp.backHomePage()
    
        hp.enterPersonalCenter()
        result=self.driver.find_element(By.XPATH,"//android.widget.TextView[@text='待付款']").text
        self.assertEqual('待付款',result)#断言是否在个人中心
        bp.backHomePage()
        result=self.driver.find_element(By.ID,'com.insthub.ecmobile:id/top_right_text').text
        self.assertEqual('通知',result)#断言是否返回主页