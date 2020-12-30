import unittest
from time import sleep

from model.browser import BroswerModel
from page.base_page import BasePage
from page.home_page import HomePage
from page.login_page import loginpage
from page.shop_page import BisinShop


class CrmShopping(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()

    # def test_addshop(self):
    #     DL=loginpage(self.driver)
    #     username,password='huachuan','admin123456'
    #     DL.login(username,password)
    #     SJ=HomePage(self.driver)
    #     SJ.shopping()
    #     ADD=BisinShop(self.driver)
    #     shopname,yiprice="yyaa",2000
    #     ADD.addshop(shopname,yiprice)
    #     sleep(5)


    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
