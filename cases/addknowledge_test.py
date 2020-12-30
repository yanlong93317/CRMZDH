import unittest
from page.home_page import HomePage
from model.browser import BroswerModel
from time import sleep
from page.base_page import BasePage
from page.login_page import LoginPage
from page.knowledgelist_page import KnowLedgeList
from page.addknowledge_page import AddknowLedge
from page.knowledge_basiclnformation import BasicInformationKL
from page.editknowledge_page import EditKnowledge
from datas.tools import data_Dl_ex


class AddProduct(unittest.TestCase):
    def setUp(self) -> None:
        lp = BroswerModel()
        self.driver = lp.broswer_chrome()
        DK = BasePage(driver=self.driver)
        DK.open()
        DL = LoginPage(driver=self.driver)
        username, password =data_Dl_ex()[0]
        DL.login(username, password)
        print("开始测试")

    @unittest.skip
    def test_1addknowledge(self):
        ZX = HomePage(driver=self.driver)
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
        self.assertIn(expect, actual, msg='添加知识失败')

    def test_2searchknowledge(self):
        ZX = HomePage(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.searchknowledgeset('云深不知处 《虞美人》')
        expect = '云深不知处 《虞美人》'
        actual = LB.addknowledgename().text
        self.assertIn(expect, actual, msg='搜索失败')

    def test_3knowledgeview(self):
        ZX = HomePage(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.searchknowledgeset('云深不知处 《虞美人》')
        LB.viewknowledge()
        JB = BasicInformationKL(driver=self.driver)
        expect = '云深不知处 《虞美人》'
        actual = JB.jbknowledgename().text
        self.assertIn(expect, actual, msg='查看失败')

    def test_4knowledgeedit(self):
        ZX = HomePage(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.editknowledge()
        BJ = EditKnowledge(driver=self.driver)
        BJ.edittitleset('云深不知处')
        expect = '云深不知处'
        actual = LB.editknowledgename().text
        self.assertIn(expect, actual, msg='编辑失败')

    def test_5deleteknowledge(self):
        ZX = HomePage(driver=self.driver)
        ZX.knowledgeset()
        LB = KnowLedgeList(driver=self.driver)
        LB.deletesets()
        LB.searchknowledgeset('云深不知处')
        expect = '----暂无数据！----'
        actual = LB.deletexiangqing().text
        self.assertIn(expect, actual, msg='删除失败')

    def tearDown(self) -> None:
        self.driver.quit()
        print('结束测试')


if __name__ == '__main__':
    unittest.main()