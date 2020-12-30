import unittest
from page.base_page import BasePage
from model.browser import BroswerModel
from page.login_page import LoginPage
from page.home_page import HomePage
from page.addtask_page import AddTask
from page.savetask_page import SaveTask
from time import sleep
from page.taskdetail_page import DetailTask
from page.edittask_page import EditTask

class AddClueTest(unittest.TestCase):
    def setUp(self) -> None:
        print('添加任务测试')
        liulan = BroswerModel()  # 实例化一个浏览器类
        self.driver = liulan.broswer_chrome()  # driver重命名
        BP = BasePage(driver=self.driver)  # 引入一个driver
        BP.open()

        DL = LoginPage(driver=self.driver)
        username, password = 'tangli', 'admin123456'
        DL.login(username, password)


    def test_1addtask(self):
        HP=HomePage(driver=self.driver)
        HP.task()

        AT=AddTask(driver=self.driver)
        AT.addtask()

        ST=SaveTask(driver=self.driver)
        ztcontent, mscontent = '考试通知', '周三接口自动化考试'
        ST.savetaskjihe(ztcontent,mscontent)
        sleep(5)
        ST.getzhuti_task()
        expect = '考试通知'
        actual = ST.getzhuti_task().text
        self.assertIn(expect, actual, msg='添加失败')


    def test_2seetask(self):
        HP = HomePage(driver=self.driver)
        HP.task()

        AT = AddTask(driver=self.driver)
        AT.see_task()
        sleep(2)

        DT=DetailTask(driver=self.driver)
        DT.get_detail()
        sleep(3)
        expect='考试通知'
        actual=DT.get_detail().text
        self.assertIn(expect,actual,msg='查看失败')


    def test_3edittask(self):
        HP = HomePage(driver=self.driver)
        HP.task()

        AT = AddTask(driver=self.driver)
        AT.see_task()
        sleep(2)

        DT = DetailTask(driver=self.driver)
        DT.alter_task()
        sleep(2)

        ET=EditTask(driver=self.driver)
        ET.alter_wancheng_task()
        sleep(2)
        ET.alter_save_task()
        sleep(2)

        AT=AddTask(driver=self.driver)
        AT.getzhuangtai_task()
        sleep(3)
        expect = '进行中'
        actual = AT.getzhuangtai_task().text
        self.assertIn(expect, actual, msg='修改失败')


    def test_4closetask(self):
        HP = HomePage(driver=self.driver)
        HP.task()

        AT = AddTask(driver=self.driver)
        AT.close_task()
        sleep(5)
        AT.getclose_task()
        sleep(2)
        expect = '已成功关闭'
        actual = AT.getclose_task().text
        self.assertIn(expect, actual, msg='关闭失败')


    def test_5deletetask(self):
        HP = HomePage(driver=self.driver)
        HP.task()
        AT = AddTask(driver=self.driver)
        AT.addtask()
        ST = SaveTask(driver=self.driver)
        ztcontent, mscontent = '元旦通知', '元旦放假安排'
        ST.savetaskjihe(ztcontent, mscontent)
        sleep(3)

        AT = AddTask(driver=self.driver)
        AT.gouxuan_task()
        AT.delete_task()
        sleep(2)
        AT.getdelete_task()
        sleep(4)
        expect = '删除成功'
        actual = AT.getdelete_task().text
        self.assertIn(expect, actual, msg='删除失败')


    def tearDown(self) -> None:
        print('添加任务成功')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


