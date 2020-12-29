import unittest
from page.home_page import Home
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import loginpage
from page.knowledgelist_page import KnowLedgeList
from page.addknowledge_page import AddknowLedge
from page.knowledge_basiclnformation import BasicInformationKL
from page.editknowledge_page import EditKnowledge


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试")

    @unittest.skip
    def test_addproduct(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.addknowledge()
        ZS = AddknowLedge(driver=self.driver)
        ZS.title('云深不知处 《虞美人》')
        ZS.iframe('我想你了')
        ZS.savesubmit()
        sleep(4)
        expect = '云深不知处 《虞美人》'
        actual = LB.addknowledgename().text
        self.assertIn(expect, actual, msg='添加产品')

        sleep(10)

    @unittest.skip
    def test_searchknowledge(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.searchknowledgeset('云深不知处 《虞美人》')
        expect = '云深不知处 《虞美人》'
        actual = LB.addknowledgename().text
        self.assertIn(expect, actual, msg='添加产品')

    @unittest.skip
    def test_knowledgeview(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.searchknowledgeset('云深不知处 《虞美人》')
        LB.viewknowledge()
        JB = BasicInformationKL(driver=self.driver)
        expect = '云深不知处 《虞美人》'
        actual = JB.jbknowledgename().text
        self.assertIn(expect, actual, msg='添加产品')

    def test_knowledgeedit(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.editknowledge()
        BJ = EditKnowledge(driver=self.driver)
        BJ.edittitleset('云深不知处')
        expect = '云深不知处'
        actual = LB.editknowledgename().text
        self.assertIn(expect, actual, msg='添加产品')

    def test_deleteknowledge(self):
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = loginpage(driver=self.driver)
        username, password = 'zhaijun', 'zj123456'
        DL.login(username, password)
        ZX = Home(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.deletesets()
        LB.searchknowledgeset('云深不知处')
        expect = '----暂无数据！----'
        actual = LB.deletexiangqing().text
        self.assertIn(expect, actual, msg='添加产品')

    def tearDown(self) -> None:
        print('结束测试')


if __name__ == '__main__':
    unittest.main()
