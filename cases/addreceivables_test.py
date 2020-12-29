import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import loginpage
from page.financelist_page import FinanceList
from page.addfinance_page import AddFinance
from page.finance_basiclnformation_page import FinanceBasiclnformation
from page.editfinance_page import EditFinance
from page.editsuccess_page import EditSuccess


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试")

    @unittest.skip
    def test_receivables(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.addfinance()
        TJ = AddFinance(driver=self.driver)
        financename, financenames, money = '天子笑', 'zhaijun', '1314'
        TJ.financenameset(financename, financenames, money)
        expect = '天子笑'
        actual = YSK.addfinanceanme().text
        self.assertIn(expect, actual, msg='添加产品')

    @unittest.skip
    def test_searchusername(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑')
        sleep(4)
        expect = '天子笑'
        actual = YSK.serchfinancename().text
        self.assertIn(expect, actual, msg='添加产品')
    @unittest.skip
    def test_viewprincipal(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('哈哈哈')
        YSK.viewfinancename()
        GG = FinanceBasiclnformation(driver=self.driver)
        expect = '哈哈哈'
        actual = GG.financenamess().text
        self.assertIn(expect, actual, msg='添加产品')

    def test_editprincipal(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑')
        YSK.editfinancename()
        BJYM=EditFinance(driver=self.driver)
        BJYM.editfinanceset('天子笑兮你一坛')
        CG=EditSuccess(driver=self.driver)
        expect = '天子笑兮你一坛'
        actual = CG.editsyccessname().text
        self.assertIn(expect, actual, msg='添加产品')

    def test_deleteprincipal(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑兮你一坛')
        YSK.deletesubmitset()


        sleep(4)



    def tearDown(self) -> None:
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
