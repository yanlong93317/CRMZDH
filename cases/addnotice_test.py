import unittest
from page.base_page import BasePage
from model.browser import BroswerModel
from page.login_page import LoginPage
from page.home_page import HomePage
from time import sleep
from page.addnotice_page import AddNotice
from page.noticedetail_page import DetailNotice
from page.editnotice_page import EditNotice

class AddMailTest(unittest.TestCase):
    def setUp(self) -> None:
        print('测试')
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)


    def test_1addmail(self):
        HP=HomePage(driver=self.driver)
        HP.tangliname()
        HP.notice()

        AN=AddNotice(driver=self.driver)
        AN.add_notice()

        DN=DetailNotice(driver=self.driver)
        btcontent='添加公告测试'
        DN.title_notice(btcontent)
        sleep(1)
        nrcontent='公告测试内容'
        DN.nrcontent_notice(nrcontent)
        sleep(1)
        DN.save_notice()
        sleep(1)
        AN.getadd_notice()
        sleep(5)
        expect = '公告添加成功'
        actual = AN.getadd_notice().text
        self.assertIn(expect, actual, msg='添加公告失败')



    def test_2seenotice(self):
        HP = HomePage(driver=self.driver)
        HP.tangliname()
        HP.notice()

        AN = AddNotice(driver=self.driver)
        AN.see_notice()

        EN=EditNotice(driver=self.driver)
        EN.getnrcontent_notice()
        sleep(5)
        expect = '公告测试内容'
        actual = EN.getnrcontent_notice().text
        self.assertIn(expect, actual, msg='查看公告失败')


    def test_3editnotice(self):
        HP = HomePage(driver=self.driver)
        HP.tangliname()
        HP.notice()

        AN = AddNotice(driver=self.driver)
        AN.see_notice()

        EN = EditNotice(driver=self.driver)
        EN.edit_notice()
        DN=DetailNotice(driver=self.driver)
        alcontent='加一句'
        DN.alterbiaoti_notice(alcontent)
        DN.save_notice()
        sleep(5)
        expect = '公告保存成功'
        actual = AN.getalcontent_notice().text
        self.assertIn(expect, actual, msg='修改保存公告失败')



    def test_4closenotice(self):
        HP = HomePage(driver=self.driver)
        HP.tangliname()
        HP.notice()
        sleep(1)

        AN = AddNotice(driver=self.driver)
        AN.tingyong_notice()
        sleep(3)
        AN.gettingyong_notice()
        sleep(5)
        expect = '修改成功，已停用'
        actual = AN.gettingyong_notice().text
        self.assertIn(expect, actual, msg='停用公告失败')


    def test_5deletenotice(self):
        HP = HomePage(driver=self.driver)
        HP.tangliname()
        HP.notice()
        sleep(1)

        AN = AddNotice(driver=self.driver)
        AN.checkbox_notice()
        AN.delete_notice()
        sleep(3)
        sercontent='添加公告测试'
        AN.serchcontent_notice(sercontent)
        sleep(1)
        AN.serch_notice()
        sleep(5)
        expect = '暂无数据'
        actual = AN.getdelete_notice().text
        print(actual)
        self.assertIn(expect, actual, msg='删除公告失败')

    def tearDown(self) -> None:
        print('成功')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


