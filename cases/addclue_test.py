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

class AddClueTest(unittest.TestCase):
    def setUp(self) -> None:
        print('添加线索测试')
    @unittest.skip
    def test_addclue(self):
        liulan=BroswerModel()      #实例化一个浏览器类
        self.driver=liulan.broswer_chrome()       #driver重命名
        BP=BasePage(driver=self.driver)       #引入一个driver
        BP.open()

        DL=LoginPage(driver=self.driver)
        username,password='tangli','admin123456'
        DL.login(username,password)

        HP=HomePage(driver=self.driver)
        HP.source()

        ADclue=AddClue(driver=self.driver)
        ADclue.addclue()

        Saclue=SaveClue(driver=self.driver)
        gsname,contactname,contens='唐丽添加线索测试','nichao','自动化好难呀'
        Saclue.sourcejihe(gsname,contactname,contens)
        sleep(5)
        expect = '唐丽添加线索测试'
        actual =ADclue.gitcluename().text
        self.assertIn(expect,actual,msg='添加失败')

    @unittest.skip
    def test_seeclue(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.seeclue()

        XQclue=ClueXiangQing(driver=self.driver)
        sleep(2)
        expect = '唐丽添加线索测试'
        actual =XQclue.getgs_xiangqing().text
        self.assertIn(expect, actual, msg='添加失败')

    @unittest.skip
    def test_editclue(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.seeclue()

        XQclue=ClueXiangQing(driver=self.driver)
        XQclue.alterclue()

        Edclue=EditClue(driver=self.driver)
        gsname='添加线索以后进行查看后再修改'
        Edclue.altergsclue(gsname)
        Edclue.altersave()

        ADclue = AddClue(driver=self.driver)
        ADclue.gitcluename()
        sleep(2)
        expect = '添加线索以后进行查看后再修改'
        actual =ADclue.gitcluename().text
        self.assertIn(expect, actual, msg='添加失败')

    @unittest.skip
    def test_transferclue(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.transferclue()
        sleep(3)
        ADclue.savetransferclue()
        sleep(3)

        HP=HomePage(driver=self.driver)
        HP.cusumer()
        sleep(3)

        TZcusumer=CusumerPage(driver=self.driver)
        TZcusumer.getlist_cusumer()
        sleep(3)
        expect = '大白兔'
        actual =TZcusumer.getlist_cusumer().text
        self.assertIn(expect, actual, msg='添加失败')
        sleep(3)


    def test_deleteallclue(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.source()

        ADclue = AddClue(driver=self.driver)
        ADclue.deletall()
        sleep(1)
        ADclue.plczclue()
        sleep(1)
        ADclue.pldeleteclue()
        sleep(2)

        ADclue.noclue()
        sleep(3)
        expect = '暂无数据'
        actual =ADclue.noclue().text
        self.assertIn(expect, actual, msg='添加失败')
        sleep(3)










    def tearDown(self) -> None:
        print('添加线索成功')


if __name__ == '__main__':
    unittest.main()
