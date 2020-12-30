import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import LoginPage
from page.financelist_page import FinanceList
from page.addfinance_page import AddFinance
from page.finance_basiclnformation_page import FinanceBasiclnformation
from page.editfinance_page import EditFinance
from page.editsuccess_page import EditSuccess
from datas.tools import data_Dl_ex


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = LoginPage(driver=self.driver)
        username, password = data_Dl_ex()[0]
        DL.login(username, password)
        print("开始测试")

    def test_1receivables(self):
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.addfinance()
        TJ = AddFinance(driver=self.driver)
        financename, financenames, money = '天子笑', 'zhaijun', '1314'
        TJ.financenameset(financename, financenames, money)
        expect = '天子笑'
        actual = YSK.addfinanceanme().text
        self.assertIn(expect, actual, msg='添加应收款失败')

    def test_2searchusername(self):
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑')
        sleep(4)
        expect = '天子笑'
        actual = YSK.serchfinancename().text
        self.assertIn(expect, actual, msg='搜索失败')

    def test_3viewprincipal(self):
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('哈哈哈')
        YSK.viewfinancename()
        GG = FinanceBasiclnformation(driver=self.driver)
        expect = '哈哈哈'
        actual = GG.financenamess().text
        self.assertIn(expect, actual, msg='查看失败')

    def test_4editprincipal(self):
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑')
        YSK.editfinancename()
        BJYM = EditFinance(driver=self.driver)
        BJYM.editfinanceset('天子笑兮你一坛')
        CG = EditSuccess(driver=self.driver)
        expect = '天子笑兮你一坛'
        actual = CG.editsyccessname().text
        self.assertIn(expect, actual, msg='编辑失败')

    def test_5deleteprincipal(self):
        ZX = HomePage(driver=self.driver)
        ZX.finance()
        YSK = FinanceList(driver=self.driver)
        YSK.searchsets('天子笑兮你一坛')
        YSK.deletesubmitset()
        YSK.searchsets('天子笑兮你一坛')
        expect = '----暂无数据！----'
        actual = YSK.deletresults().text
        self.assertIn(expect, actual, msg='删除失败')

    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
