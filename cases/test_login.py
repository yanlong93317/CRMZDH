from page.login_page import LoginPage   #调用自己所写的类
from page.home_page import Homepage     #调用自己所写的类
from cases.base_case import BaseCase    #调用自己所写的类
import unittest   #引入自动化测试框架
from model import login_excel           #调用自己所写的类
from model import login_csv            #调用自己所写的类
class TestLogin(BaseCase):           #定义一个类用于测试
    def test_login_en(self):        #定义一个函数用于登录
        lp=LoginPage(self.driver)      #调用类用与输入数据
        # username,password=login_excel.read_excel()[0]   #调用类，使用参数
        # username, password = login_csv.readcsv()[0]     #调用类，使用参数
        # lp.login(username,password)
        lp.login("admin","admin123456") #登录，数据来源于变量
        #断言
        hp=Homepage(self.driver)            #调用类，打开网页并找到需要断言的目标
        text=hp.get_username_text()    #将需要断言的目标文本提前出来
        # self.assertEqual(text, "线索")
        if text=="线索":      #判断，进行断言
            print("成功")
        else:
            raise AssertionError("登录失败")

if __name__=="__main__":
    unittest.main()    #开始执行用例