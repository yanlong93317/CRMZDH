import unittest
from time import sleep

from model.browser import BroswerModel
from page import huachuan
from page.base_page import BasePage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.pan_page import MyPanel


class CrmPanel(unittest.TestCase):
    def setUp(self):
        '''打开登录页面'''
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        dk = BasePage(driver=self.driver)
        dk.open()

    def test_1addpan(self):
        '''增加组件'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        ADD = MyPanel(self.driver)
        panname = huachuan.loginuser('datas')[2][1]
        ADD.addpan(panname)
        sleep(3)
        if panname in ADD.mouduss():
            print("测试成功")
        else:
            raise AssertionError("测试失败")


    def test_2after(self):
        '''修改组件名'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        ADD = MyPanel(self.driver)
        elename_ago=ADD.alterzjm()
        panname = huachuan.loginuser('datas')[4][1]
        ADD.alter_ele(panname)
        sleep(3)
        elename_rear=ADD.alterzjm()
        if elename_ago != elename_rear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_3addsched(self):
        '''增加日程'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        ADD = MyPanel(self.driver)
        schename = huachuan.loginuser('datas')[2][1]
        ADD.addschedule(schename)
        sleep(3)
        sche=ADD.seche()
        if sche==schename:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_4checknotice(self):
        '''查看公告'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        NOTICE = MyPanel(self.driver)
        NOTICE.notice()
        sleep(3)
        if "添加公告"==NOTICE.sche():
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_5checkbunsin(self):
        '''查看商机统计'''
        DL = LoginPage(self.driver)
        username, password = huachuan.loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.pan()
        BUNSESS = MyPanel(self.driver)
        BUNSESS.bunsinsta()
        sleep(3)
        if "商机统计报表"==BUNSESS.shopstatic():
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
