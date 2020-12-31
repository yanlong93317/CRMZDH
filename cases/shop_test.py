import unittest
from time import sleep

from model.browser import BroswerModel
from datas.tools import *
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
        '''商机添加'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        ADD = BisinShop(self.driver)
        shopname, yiprice =datas('business')[3]
        ADD.addshop(shopname, int(yiprice))
        sleep(1)
        if shopname ==ADD.shopadd():
            print("测试成功")
        else:
            raise AssertionError("测试失败")


    def test_2editshop(self):
        '''商机编辑'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        ADD = BisinShop(self.driver)
        price=datas('business')[9][1]
        ADD.editshop(int(price))
        sleep(5)
        if ADD.yujiprice()==price:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def test_3serachshop(self):
        '''搜索'''
        DL = LoginPage(self.driver)
        username, password =loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        search_ago=SERACH.djnumber()
        srar=datas('search')[2]
        SERACH.serach(srar)
        sleep(1)
        search_sear = SERACH.djnumber()
        if search_ago != search_sear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
    #
    def test_4shopbost(self):
        '''推进'''
        DL = LoginPage(self.driver)
        username, password =loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        SERACH.djboost()
        SERACH.stage(3)
        boost_ago=SERACH.stge(3)
        SERACH.boost()
        sleep(1)
        boost_sear=SERACH.status()
        if boost_ago==boost_sear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")
    #
    def test_5shopdel(self):
        '''商机删除'''
        DL = LoginPage(self.driver)
        username, password = loginuser('login')[2]
        DL.login(username, password)
        SJ = HomePage(self.driver)
        SJ.shopping()
        SERACH = BisinShop(self.driver)
        del_ago = SERACH.djnumber()
        SERACH.delshop()
        sleep(1)
        del_sear = SERACH.djnumber()
        if del_ago != del_sear:
            print("测试成功")
        else:
            raise AssertionError("测试失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
