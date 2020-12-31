import unittest
from time import sleep

from model.browser import BroswerModel
from page.auth_page import MyAuth
from page.base_page import BasePage
from page.home_page import HomePage
from datas.tools import *
from page.login_page import LoginPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()

    def test_1depart(self):
        '''增加岗位'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        ADDdepart = MyAuth(self.driver)
        dpart = datas('datas')[6][0]
        aa = dpart[0]
        ADDdepart.adddepart(dpart)
        act = ADDdepart.dpart(aa)
        sleep(1)
        if act == "成功":
            print("测试通过")
        else:
            raise AssertionError("失败")

    def test_2nextpage(self):
        '''下一页'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        NEXT = MyAuth(self.driver)
        NEXT.useradmin()
        click_rea = NEXT.nummer()
        NEXT.nestpage()
        sleep(1)
        clicks = NEXT.nummer()
        if click_rea != clicks:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_3editinfo(self):
        '''修改用户信息'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        EDIt = MyAuth(self.driver)
        EDIt.useradmin()
        edit_age = EDIt.phone(4, 0)
        phone = datas('datas')[6][3]
        EDIt.edituserinfo(int(phone))
        sleep(1)
        SJ.auth()
        sleep(1)
        EDIt.useradmin()
        edit_rear = EDIt.phone(4, 0)
        if edit_age != edit_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
        sleep(6)

    def test_4checkuser(self):
        '''翻页'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        CHECK = MyAuth(self.driver)
        CHECK.useradmin()
        click_rea = CHECK.nummer()
        CHECK.checkalluser()
        sleep(1)
        clicks = CHECK.nummer()
        if click_rea != clicks:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_5addadminyser(self):
        '''增加管理员'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.auth()
        Adduser = MyAuth(self.driver)
        adminname, adminpasswd = loginuser('adminlogin')[5]
        Adduser.adduseradmin(adminname, adminpasswd)
        sleep(1)
        add_age = Adduser.phone(2, -1)
        add_ag = add_age.strip()
        print(adminname)
        if adminname == add_ag:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
