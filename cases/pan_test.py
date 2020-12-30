import unittest
from time import sleep

from model.browser import BroswerModel
from page.base_page import BasePage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.pan_page import MyPanel
from page.shop_page import BisinShop


class CrmPanel(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()
    def test_addpan(self):
        DL = LoginPage(self.driver)
        username, password = 'huachuan', 'admin123456'
        DL.login(username, password)
        SJ=HomePage(self.driver)
        SJ.pan()
        ADD=MyPanel(self.driver)
        panname="yyaa"
        ADD.addpan(panname)
        sleep(5)
    def test_after(self):
        DL = LoginPage(self.driver)
        username, password = 'huachuan', 'admin123456'
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        ADD = MyPanel(self.driver)
        panname = "yyaa"
        ADD.alter_ele(panname)
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
