import unittest
from time import sleep

from model.browser import BroswerModel
from page import huachuan
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
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        lp.addcont(300)

    def test_2editcont(self):
        '''商机修改'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        lp.editcont(100)
        sleep(4)

    def test_3searchcont(self):
        '''搜索'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        lp.search(300)
        sleep(4)

    def test_4contnext(self):
        '''下一页'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        lp.checknext()
        sleep(4)

    def test_5contdel(self):
        '''删除合同'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp = MyCont(self.driver)
        lp.delcont()
        sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
