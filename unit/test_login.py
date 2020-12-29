from selenium import webdriver     #引入浏览器模块
from selenium.webdriver.common.by import By   #引入By类
from time import sleep     #引入时间模块
import unittest      #引入自动化框架
from unit import login_date     #调用类
from unit import sql            #调用类
from unit import logincsv       #调用类
# class MyTest_unittest(unittest.TestCase):   #定义一个类，
#     def setUp(self):
#         self.driver = webdriver.Chrome()    #浏览器实例化
#         self.driver.get("http://localhost:8080/upload/admin")  #打开网址
#     def test_login_cn(self):   #定一个函数，用于登录
#         # username,password,locator= login_date.read_excel()[1]   #调用参数，变量名来源于参数
#         username, password, locator =sql.hhh()[0]        #调用参数，变量名来源于参数
#         # username, password, locator =logincsv.read_csv()[1]      #调用参数，变量名来源于参数
#         loc = (By.NAME, "username")      #定义定位器
#         pas = (By.NAME, "password")      #定义定位器
#         sub = (By.CSS_SELECTOR, "input[value='进入管理中心']")     #定义定位器
#         self.driver.find_element(*loc).send_keys(username)       #找到用户名输入框输入数据
#         self.driver.find_element(*pas).send_keys(password)       #找到密码输入框输入数据
#         sleep(2)
#         self.driver.find_element(*sub).click()      #按钮点击
#         ul=self.driver.current_url    #定义需要断言的变量名
#         self.assertIn(ul,locator)      #设置断言类型
#         self.driver.switch_to.frame("header-frame")   #找到需要断言的那一栏
#         bb=self.driver.find_element(By.CSS_SELECTOR,"#submenu-div > ul > "
#                                 "li:nth-child(1) > a > span").text  #找到断言目标，并提取出它的文本
#         if bb=="退出":    #判断，进行断言
#             print("成功")
#         else:
#             raise AssertionError("失败")
#         sleep(5)
#         self.driver.quit()   #浏览器退出
#     @unittest.skip("跳过")
#     def test_login_zn(self):
#         loc = (By.NAME, "username")
#         pas = (By.NAME, "password")
#         sub = (By.CSS_SELECTOR, "body > form > table > tbody > tr:nth-child(2)"
#                                 " > td > table > tbody > tr:nth-child(5) >"
#                                 " td:nth-child(2) > input")
#         self.driver.find_element(*loc).send_keys("张三")
#         self.driver.find_element(*pas).send_keys("admin123456")
#         sleep(2)
#         self.driver.find_element(*sub).click()
#         sleep(3)
#     def tearDown(self):    #最后定义一个函数，用于清理之前的操作
#             print("清理")
# if __name__=="__main__":
#     unittest.main()       #开始执行测试用例
from selenium import webdriver     #引入浏览器模块
driver=webdriver.Chrome()      #选择要用到的浏览器并设置为变量名
def login(name,passwd):     #定义一个函数
    driver.find_element_by_name("username").send_keys(name)   #找到用户名输入框并输入变量
    driver.find_element_by_name("password").send_keys(passwd)  #找到密码输入框并输入变量
    driver.find_element_by_class_name("btn-a").click()   #找到按钮并进行点击