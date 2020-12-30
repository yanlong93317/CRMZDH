import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import LoginPage
from page.home_page import HomePage
from page.systemsettings_page import SystemSettings


class AddField(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = LoginPage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        print("开始测试")

    @unittest.skip
    def test_1addfiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        logoname, enterprompt = '外婆的道歉信', '张欢的书店'
        SYS.addfieldset(logoname, enterprompt)
        expect = '外婆的道歉信'
        name = '外婆的道歉信'
        actual = SYS.gettext(name).text
        self.assertIn(expect, actual, msg='添加字段成功')

    def test2_editfiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        logoname = '客户名称520'
        SYS.editlogonameset(logoname)
        expect = '客户名称520'
        actual = SYS.getfristkehuname().text
        self.assertIn(expect, actual, msg='编辑字段失败')

    @unittest.skip
    def test_3listdisplay(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        SYS.listdisply()
        expect = '取消列表显示'
        actual = SYS.cancellistdispaly().text
        self.assertIn(expect, actual, msg='显示列表失败')

    def test_4deletefiled(self):
        ZX = HomePage(driver=self.driver)
        ZX.systemset()
        SYS = SystemSettings(driver=self.driver)
        SYS.modulesettings()
        names = '外婆的道歉信'
        SYS.locationlogoname(names)
        print(1111)
        expect = '删除自定义字段成功'
        actual = SYS.deletereault().text
        self.assertIn(expect, actual, msg='显示列表失败')

    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
