import unittest
from time import sleep

from model.browser import BroswerModel
from page import huachuan
from page.base_page import BasePage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.shop_page import BisinShop


class CrmShopping(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()

    def test_1addshop(self):
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        ADD = BisinShop(self.driver)
        shopname, yiprice = "yyaa", 2000
        ADD.addshop(shopname, yiprice)
        sleep(5)

    def test_2editshop(self):
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        ADD = BisinShop(self.driver)
        ADD.editshop(6000)
        sleep(5)

    def test_3serachshop(self):
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        SERACH.serach("yy")
        sleep(5)

    def test_4shopbost(self):
        '''推进'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        SERACH.boost(2)
        sleep(6)

    def test_5shopdel(self):
        '''商机推进'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        SERACH.delshop()
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
