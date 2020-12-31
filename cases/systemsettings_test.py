import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import LoginPage
from page.home_page import HomePage
from page.systemsettings_page import SystemSettings
from datas.tools import *


class AddField(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = LoginPage(driver=self.driver)
        username, password = data_Dl_ex()[0]
        DL.login(username, password)
        print("开始测试")


    def test_1addfiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        logoname, enterprompt, expect, actual = data_systemsettings_ex()[0]
        SYS.addfieldset(logoname, enterprompt)
        expect = expect
        actual = SYS.gettext(actual).text
        self.assertIn(expect, actual, msg='添加字段成功')

    def test2_editfiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        SYS.editlogonameset(data_systemsettings_ex()[1][0])
        expect = data_systemsettings_ex()[1][2]
        actual = SYS.getfristkehuname().text
        self.assertIn(expect, actual, msg='编辑字段失败')

    @unittest.skip
    def test_3listdisplay(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        SYS.listdisply()
        expect = data_systemsettings_ex()[2][2]
        actual = SYS.cancellistdispaly().text
        self.assertIn(expect, actual, msg='显示列表失败')

    def test_4deletefiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        SYS.locationlogoname(data_systemsettings_ex()[0][0])
        expect = '删除自定义字段成功'
        actual = SYS.deletereault().text
        self.assertIn(expect, actual, msg='显示列表失败')

    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
