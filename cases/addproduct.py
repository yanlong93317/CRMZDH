# -*- coding: utf-8 -*-
# @Time : 2020/12/28 15:54
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : addproduct.py
# @Project : CRMZDH
import unittest
from page.home_page import Home
from model.browser import BroswerModel
from time import sleep
from page.addgoods_page import AddGoods
from page.productlist_page import ProductList
from page.login_page import loginpage
from page.base_page import BasePage


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试")

    def test_addproduct(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowlege()
        ZS = ProductList(driver=self.driver)
        ZS.addproduct()
        Ad = AddGoods(driver=self.driver)
        goodsname, developmentteam = '天子笑', '云生不知处'
        Ad.addgoodset(goodsname, developmentteam)
        sleep(6)
        expect = '天子笑'
        actual = ZS.prductname().text
        self.assertIn(expect, actual, msg='添加产品')

    def tearDown(self) -> None:
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
