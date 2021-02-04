import unittest
from page.base_page import BasePage
from model.browser import BroswerModel
from page.login_page import LoginPage
from page.home_page import HomePage
from page.addclue_page import AddClue
from page.savesource_page import SaveClue
from time import sleep
from page.xsxiangqing_page import ClueXiangQing
from page.editclue_page import EditClue
from page.cusumer_page import CusumerPage
from page.savesource_page import SaveClue
from datas.tools import *


class AddClueTest(unittest.TestCase):
    def setUp(self) -> None:
        print('添加线索测试')
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password =data_Dl_ex()[1]
        DL.login(username, password)


    def test_1addclue(self):
        HP=HomePage(driver=self.driver)
        HP.source()

        ADclue=AddClue(driver=self.driver)
        ADclue.addclue()

        Saclue=SaveClue(driver=self.driver)
        Saclue.laiyuan()
        sleep(4)
        gsname, contactname, contens,expect=data_clue_ex()[2]
        Saclue.sourcejihe(gsname,contactname,contens)
        sleep(5)
        expect = expect
        actual =ADclue.gitcluename().text
        self.assertIn(expect,actual,msg='添加失败')


    def test_2seeclue(self):
        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.seeclue()

        XQclue=ClueXiangQing(driver=self.driver)
        sleep(2)
        expect = data_clue_ex()[1][2]
        expect = expect
        actual =XQclue.getgs_xiangqing().text           #详情页面中的公司名
        self.assertIn(expect, actual, msg='查看失败')


    def test_3editclue(self):

        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.seeclue()

        XQclue=ClueXiangQing(driver=self.driver)
        XQclue.alterclue()

        Edclue=EditClue(driver=self.driver)
        sleep(3)
        gsname, expect = data_clue_ex()[2][1],data_clue_ex()[2][4],
        gsname=gsname                    #修改为雪
        Edclue.altergsclue(gsname)
        Edclue.altersave()

        ADclue = AddClue(driver=self.driver)
        ADclue.gitcluename()
        sleep(2)
        expect = expect
        actual =ADclue.gitcluename().text
        self.assertIn(expect, actual, msg='修改失败')


    def test_4transferclue(self):
        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        sleep(5)
        ADclue.transferclue()
        sleep(3)
        CR = CusumerPage(driver=self.driver)
        sleep(5)
        gsname=data_clue_ex()[3][2]
        CR.tansfer_kehu(gsname)
        CR.savetransferclue()
        sleep(3)
        ADclue = AddClue(driver=self.driver)
        expect = data_clue_ex()[3][4]
        sleep(4)
        expect = expect
        actual =ADclue.gittransfer().text
        self.assertIn(expect, actual, msg='转换失败')
        sleep(3)


    def test_5deleteallclue(self):
        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.addclue()

        Saclue=SaveClue(driver=self.driver)
        Saclue.laiyuan()
        sleep(1)
        gsname, contactname, contens ,expect= data_clue_ex()[4][0],data_clue_ex()[4][1],data_clue_ex()[4][2],data_clue_ex()[4][3],
        Saclue.sourcejihe(gsname, contactname, contens)
        #以上因为没有线索了得再新建一条线索
        ADclue = AddClue(driver=self.driver)
        ADclue.deletall()
        sleep(1)
        ADclue.plczclue()
        sleep(1)
        ADclue.pldeleteclue()
        sleep(5)
        expect = expect
        actual =ADclue.noclue().text
        self.assertIn(expect, actual, msg='删除失败')
        sleep(3)


    def tearDown(self) -> None:
        print('添加线索成功')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
