import unittest
from time import sleep

from model.browser import BroswerModel
from page.auth_page import MyAuth
from page.base_page import BasePage
from page.home_page import HomePage
from page import huachuan
from page.login_page import LoginPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()
    #
    def test_1depart(self):
        '''增加岗位'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        ADDdepart = MyAuth(self.driver)
        depart=huachuan.loginuser('departname')[1]
        ADDdepart.adddepart(depart)
    #
    # def test_2nextpage(self):
    #     DL = LoginPage(self.driver)
    #     username, password = huachuan.loginuser('login')[2]
    #     DL.login(username, password)
    #     SJ = HomePage(self.driver)
    #     SJ.auth()
    #     NEXT = MyAuth(self.driver)
    #     NEXT.nextpge()
    #     sleep(5)
    #
    # def test_3editinfo(self):
    #     DL = LoginPage(self.driver)
    #     username, password = huachuan.loginuser('login')[2]
    #     DL.login(username, password)
    #     SJ = HomePage(self.driver)
    #     SJ.auth()
    #     NEXT = MyAuth(self.driver)
    #     NEXT.edituserinfo("14356547875")
    #     sleep(2)
    #     SJ.auth()
    #     sleep(3)
    #     NEXT.useradmin()
    #     sleep(6)
    # #
    # def test_4checkuser(self):
    #     DL = LoginPage(self.driver)
    #     username, password = huachuan.loginuser('login')[2]
    #     DL.login(username, password)
    #     SJ = HomePage(self.driver)
    #     SJ.auth()
    #     NEXT = MyAuth(self.driver)
    #     NEXT.checkalluser()
    #     sleep(3)
    #
    # def test_5addadminyser(self):
    #     DL = LoginPage(self.driver)
    #     username, password = huachuan.loginuser('login')[2]
    #     DL.login(username, password)
    #     SJ = HomePage(self.driver)
    #     SJ.auth()
    #     NEXT = MyAuth(self.driver)
    #     adminname, adminpasswd = "eeewwww", "123456"
    #     NEXT.adduseradmin(adminname, adminpasswd)
    #     sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
