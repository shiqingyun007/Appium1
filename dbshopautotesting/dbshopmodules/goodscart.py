# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2021-12-16 9:54
# Software:PyCharm
# File:goodscart.py

import time
from selenium.webdriver.common.by import By
from dbshopautotesting.dbshopmodules.back import Back
from dbshopautotesting.dbshopmodules.shipping_address import ShippingAddress

# 购物车相关操作
class GoodsCart:

    def __init__(self,driver,action):
        self.driver=driver
        self.action=action

    # 修改商品数量
    def modify_goodsNum(self):
        self.driver.tap([(600, 160)], 1)  # 点击修改
        time.sleep(2)
        self.driver.tap([(600, 200)], 1)  # 增加1个商品
        time.sleep(1)
        self.driver.tap([(450, 200)], 1)
        time.sleep(1)
        self.driver.tap([(450, 200)], 1)  # 再减少2个商品
        time.sleep(1)
        self.driver.tap([(300, 150)], 1)  # 点击完成
        time.sleep(4)

    # 未添加收货地址，点击结算，跳转至新增收货地址界面
    def buttonCloseAccount(self):
        self.action.tap(None,630,420).wait(3000).perform() #点击 结算

        #判断是否有地址，无地址添加地址
        if self.driver.find_elements(By.ID,'com.insthub.ecmobile:id/add_address_name')!=[]:
            ShippingAddress(self.driver,self.action).addAddressInfo()
            self.action.tap(None, 630, 420).wait(3000).perform()# 添加收货地址后，再点击结算