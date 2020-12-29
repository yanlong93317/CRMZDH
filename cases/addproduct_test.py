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
from page.login_page import loginpage
from page.base_page import BasePage
from page.goods_basicInformation_page import BasicInformation
from page.puduct_edit_page import PuductEdit


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        print("开始测试")

    def test_1addproduct(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.addproduct()
        Ad = AddGoods(driver=self.driver)
        goodsname, developmentteam = '天子笑', '云生不知处'
        Ad.addgoodset(goodsname, developmentteam)
        sleep(6)
        expect = '天子笑'
        actual = ZS.prductname().text
        self.assertIn(expect, actual, msg='添加产品')


    def test_2search(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.searchset('十全大补丸')
        sleep(4)
        expect = '十全大补丸'
        actual = ZS.productnames().text
        self.assertIn(expect, actual, msg='添加产品')


    def test_3view(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.searchset('十全大补丸')
        ZS.view()
        XX=BasicInformation(driver=self.driver)
        expect = '十全大补丸'
        actual = XX.basicInformationshopname().text
        print(actual)
        self.assertIn(expect, actual, msg='添加产品')


    def test_4edit(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.searchset('张欢')
        ZS.edit()
        BJ=PuductEdit(driver=self.driver)
        BJ.editset('张欢')
        sleep(10)
        expect = '张欢'
        actual = ZS.zhanghaun('张欢').text
        print(actual)
        self.assertIn(expect, actual, msg='添加产品')

    def test_5delete(self):
        ZX = HomePage(driver=self.driver)
        ZX.puducts()
        ZS = ProductList(driver=self.driver)
        ZS.search('天子笑')
        ZS.searchsubmit()
        ZS.xuanzesubmit()
        sleep(1)
        ZS.deletesubmit()
        ZS.searchset('天子笑')
        sleep(3)
        ZS.deletresult()
        expect = '----暂无数据！----'
        actual = ZS.deletresult().text
        print(actual)
        self.assertIn(expect, actual, msg='添加产品')

        sleep(3)











    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()