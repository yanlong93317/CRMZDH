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

