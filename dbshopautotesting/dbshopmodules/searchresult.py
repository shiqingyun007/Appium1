# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-17 17:20
# Software:PyCharm
# File:searchresult.py
import random
import time
from selenium.webdriver.common.by import By
#搜索结果页相关操作
from dbshopautotesting.dbshopmodules.login import Login
from dbshopautotesting.dbshopmodules.search import Search


class SearchResult:
    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    # 搜索结果页相关操作
    def resetSearchResult(self):
        # 判断搜索结果页中是否有商品，没有返回搜索模块，继续重新操作，直到进入有商品的模块后退出循环
        while self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='没有结果']") != []:
            for i in range(2):
                self.driver.press_keycode(4)
                time.sleep(3)
            Search(self.driver,self.action).randomEnter()

    # 上滑加载商品资源
    def loadGoods(self):
        self.driver.swipe(360,800,360,200)
        time.sleep(3)

    # 切换人气排行
    def changeSort(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/filter_title_tabone').click()
        time.sleep(3)
        self.loadGoods()

    # 点击 筛选，选择 全部价格
    def selectConfig(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/search_filter').click()
        time.sleep(3)

        lis=self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/specification_value_text_one')
        if len(lis)==9:#主页手机类型或搜索-手机类型-GSM手机进入，第一列有9个选项
            lis[6].click()#点击全部价格
        if len(lis)==4:#搜索-手机类型-3G手机/双模手机 进入，第一列有4个选项
            lis[2].click()#
        elif len(lis)==2:
            lis[1].click()#点击索爱
        else:
            pass#找不到任何元素，不做任何操作
        time.sleep(3)

        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/top_right_button').click()
        time.sleep(3)

    # 遍历整个页面的所有商品
    def viewAllGoods(self):
        elements = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/gooditem_photo')
        for i in elements:
            i.click()
            time.sleep(3)
            self.driver.press_keycode(4)
            time.sleep(3)

    # 随机选择一个商品进入其详情页面
    def randomEnterGoodDetail(self):
        elements = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/gooditem_photo')
        num = random.randint(0, len(elements) - 1)
        elements[num].click()
        time.sleep(3)

    # 进入购物车
    def enterGoodsCart(self):
        self.driver.find_element(By.ID,'com.insthub.ecmobile:id/good_list_shopping_cart').click()
        time.sleep(3)
        # 判断是否登录
        if self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/login_name') != []:
            Login(self.driver).login()
            time.sleep(2)
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/good_list_shopping_cart').click()
            time.sleep(3)
