# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0:10
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : addknowledge_test.py
# @Project : CRMZDH
import unittest
from page.home_page import Home
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import loginpage
from page.knowledgelist_page import KnowLedgeList
from page.addknowledge_page import AddknowLedge


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
        ZX.knowledgeset()
        LB=KnowLedgeList(driver=self.driver)
        LB.addknowledge()
        ZS=AddknowLedge(driver=self.driver)
        ZS.title('云深不知处 《虞美人》')

    def tearDown(self) -> None:
        print('结束测试')

    if __name__ == '__main__':
        unittest.main()
