# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-15 17:34
# Software:PyCharm
# File:testcaseone.py
import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from dbshopautotesting.dbshopflows.flowfive import FlowFive
from dbshopautotesting.dbshopflows.flowfour import FlowFour
from dbshopautotesting.dbshopflows.flowone import FlowOne
from dbshopautotesting.dbshopflows.flowsix import FlowSix
from dbshopautotesting.dbshopflows.flowthree import FlowThree
from dbshopautotesting.dbshopflows.flowtwo import FlowTwo
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.homepage import HomePage
from dbshopautotesting.dbshopmodules.welcomepage import WelcomePage


class TestCaseOne(unittest.TestCase):

    def setUp(self) -> None:
        desired_cap={
            'platformName':'Android',
            'platformVersion':'7.1.2',
            'deviceName':'Android enumlator',
            'appPackage':'com.insthub.ecmobile',
            'appActivity':'com.insthub.BeeFramework.activity.StartActivity',
            'noReset':False,
            'unicodeKeyboard':True,
            'resetKeyboard':True
        }

        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
        self.action=TouchAction(self.driver)



    def test(self):
        # 判断是否有欢迎界面
        if self.driver.find_elements(By.ID,'com.insthub.ecmobile:id/good_cell_photo_two')==[]:
            WelcomePage(self.driver).fiveSwipe()

        # 测试流程1：主页的相关操作
        # FlowOne(self.driver).flowOne()

        # 测试流程2：商品详情页的相关操作
        # FlowTwo(self.driver,self.action).flowTwo()

        # 测试流程3：搜索相关操作
        # FlowThree(self.driver,self.action).flowThree()

        # 测试流程4：搜索结果页相关操作
        # FlowFour(self.driver,self.action).flowFour()

        # 测试流程5：搜索与首页、购物车之间页面切换
        # FlowFive(self.driver,self.action).flowFive()

        # 测试流程6：主页-》商品详情-》购物车-》结算
        FlowSix(self.driver,self.action).flowSix()
    def tearDown(self) -> None:
        pass
        # self.driver.quit()