# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0:00
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : addproduct_test.py
# @Project : CRMZDH
import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.addgoods_page import AddGoods
from page.productlist_page import ProductList
from page.login_page import LoginPage
from page.base_page import BasePage
from page.goods_basicInformation_page import BasicInformation
from page.puduct_edit_page import PuductEdit
from datas.tools import *


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = LoginPage(driver=self.driver)
        username, password = data_Dl_ex()[0]
        DL.login(username, password)
        print("开始测试")

    def test_1addproduct(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.addproduct()
        Ad = AddGoods(driver=self.driver)
        goodsname, developmentteam, expect = data_product_ex()[0][:3]
        Ad.addgoodset(goodsname, developmentteam)
        sleep(6)
        expect = expect
        actual = ZS.prductname().text
        self.assertIn(expect, actual, msg='添加产品失败')

    def test_2search(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        expect, name = data_product_ex()[0][3], data_product_ex()[1][2]
        ZS.searchset(name)
        sleep(4)
        expect = expect
        actual = ZS.productnames().text
        self.assertIn(expect, actual, msg='搜索失败')

    def test_3view(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.searchset(data_product_ex()[0][3])
        ZS.view()
        XX = BasicInformation(driver=self.driver)
        expect = data_product_ex()[1][2]
        actual = XX.basicInformationshopname().text
        print(actual)
        self.assertIn(expect, actual, msg='查看失败')

    def test_4edit(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.searchset(data_product_ex()[1][3])
        ZS.edit()
        BJ = PuductEdit(driver=self.driver)
        BJ.editset(data_product_ex()[1][3])
        sleep(10)
        expect = data_product_ex()[2][3]
        actual = ZS.zhanghaun(data_product_ex()[0][4]).text
        print(actual)
        self.assertIn(expect, actual, msg='编辑失败')

    def test_5delete(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.search(data_product_ex()[0][0])
        ZS.searchsubmit()
        ZS.xuanzesubmit()
        sleep(1)
        ZS.deletesubmit()
        ZS.searchset(data_product_ex()[0][0])
        sleep(3)
        ZS.deletresult()
        expect = data_product_ex()[3][2]
        actual = ZS.deletresult().text
        print(actual)
        self.assertIn(expect, actual, msg='删除失败')

    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
