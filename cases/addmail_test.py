import unittest
from page.base_page import BasePage
from model.browser import BroswerModel
from page.login_page import LoginPage
from page.home_page import HomePage
from time import sleep
from page.addmail_page import AddMail
from page.maildetail_page import DetailMail

class AddMailTest(unittest.TestCase):
    def setUp(self) -> None:
        print('写信测试')

    @unittest.skip
    def test_addmail(self):
        liulan=BroswerModel()      #实例化一个浏览器类
        self.driver=liulan.broswer_chrome()       #driver重命名
        BP=BasePage(driver=self.driver)       #引入一个driver
        BP.open()

        DL=LoginPage(driver=self.driver)
        username,password='tangli','admin123456'
        DL.login(username,password)

        HP=HomePage(driver=self.driver)
        HP.more()
        HP.mail()

        AM=AddMail(driver=self.driver)
        nrcontent='考试通知'
        AM.addmailjihe(nrcontent)
        sleep(3)
        AM.getnr_mail()
        sleep(5)
        expect = '考试通知'
        actual = AM.getnr_mail().text
        self.assertIn(expect, actual, msg='写信失败')


    @unittest.skip
    def test_seemail(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.more()
        HP.mail()

        AM = AddMail(driver=self.driver)
        AM.see_mail()
        sleep(2)

        DM=DetailMail(driver=self.driver)
        DM.getcontent_mail()
        sleep(5)
        expect = '考试通知'
        actual = DM.getcontent_mail().text
        self.assertIn(expect, actual, msg='写信失败')

    @unittest.skip
    def test_replymail(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.more()
        HP.mail()

        AM = AddMail(driver=self.driver)
        AM.see_mail()
        sleep(2)

        DM = DetailMail(driver=self.driver)
        DM.reply_mail()
        reeecontent='知道了'
        sleep(2)
        DM.replycontent_mail(reeecontent)
        DM.replysend_mail()

        AM=AddMail(driver=self.driver)
        sleep(3)
        AM.inbox_mail()
        sleep(3)
        AM.gerycontent_mail()
        sleep(5)
        expect = '知道了'
        actual = AM.gerycontent_mail().text
        self.assertIn(expect, actual, msg='回复失败')


    @unittest.skip
    def test_yidumail(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.more()
        HP.mail()

        AM = AddMail(driver=self.driver)
        AM.checkbox_mail()
        sleep(2)
        AM.piliang_mail()
        sleep(1)
        AM.yidu_mail()
        sleep(1)
        AM.getyidu_mail()
        sleep(5)
        expect = '设置已读成功'
        actual = AM.getyidu_mail().text
        self.assertIn(expect, actual, msg='设置已读失败')



    def test_deletemail(self):
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)

        HP = HomePage(driver=self.driver)
        HP.more()
        HP.mail()

        AM = AddMail(driver=self.driver)
        AM.checkbox_mail()
        sleep(2)
        AM.piliang_mail()
        sleep(1)
        AM.delete_mail()
        sleep(1)
        AM.getdelete_mail()
        sleep(5)
        expect = '删除成功'
        actual = AM.getdelete_mail().text
        self.assertIn(expect, actual, msg='删除失败')




    def tearDown(self) -> None:
        print('写信成功')


if __name__ == '__main__':
    unittest.main()


