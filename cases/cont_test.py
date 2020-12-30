import unittest
from time import sleep

from model.browser import BroswerModel
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

    # def test_addpan(self):
    #     DL = LoginPage(self.driver)
    #     username, password = 'huachuan', 'admin123456'
    #     DL.login(username, password)
    #     CONT = HomePage(self.driver)
    #     CONT.cont()
    #     lp=MyCont(self.driver)
    #     lp.addcont(300)
    def test_editpan(self):
        DL = LoginPage(self.driver)
        username, password = 'huachuan', 'admin123456'
        DL.login(username, password)
        CONT = HomePage(self.driver)
        CONT.cont()
        lp=MyCont(self.driver)
        lp.editcont(100)
        sleep(4)



if __name__ == '__main__':
    unittest.main()
