import unittest
from time import sleep

from model.browser import BroswerModel
from datas.tools import *
from page.base_page import BasePage
from page.cont_page import MyCont
from page.home_page import HomePage
from page.login_page import LoginPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()

    def test_1addcont(self):
        '''增加合同'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        yeshu_age = lp.contfy()
        price = datas("business")[3][1]
        lp.addcont(int(price))
        sleep(1)
        yeshu_rear = lp.contfy()
        sleep(1)
        if yeshu_age != yeshu_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_2editcont(self):
        '''商机修改'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        EDIT = MyCont(self.driver)
        price = datas('business')[6][1]
        EDIT.editcont(int(price))
        sleep(1)
        money = EDIT.money()
        if money == price:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_3searchcont(self):
        '''搜索'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        sear_age = lp.contfy()
        lp.search(9)
        sleep(1)
        sear_rear = lp.contfy()
        sleep(1)
        if sear_age != sear_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
        sleep(1)

    def test_4contnext(self):
        '''下一页'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        dj_age = lp.contfy()
        lp.checknext()
        dj_rear = lp.contfy()
        sleep(1)
        if dj_age != dj_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
        sleep(1)

    def test_5contdel(self):
        '''删除合同'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        del_age = lp.contfy()
        lp.delcont()
        sleep(1)
        del_rear = lp.contfy()
        sleep(1)
        if del_age != del_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
        sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
