from selenium import webdriver
from selenium.webdriver.common.by import By
# class Login():
#     def __init__(self,driver):
#         self.driver=driver
#         self.url="http://localhost:8080/upload/admin"  #定义url
#         #定义定位器
#         self.login_username_loc=(By.NAME,"username")
#         self.login_password_loc = (By.NAME, "password")
#         self.login_button_loc = (By.NAME, "btn-a")
#     def open(self):
#         #打开url
#         self.driver.get(self.url)
#         self.driver.impplictly_wait(self.time)
#     def login_username(self,uname):
#         #用户名输入框
#         self.driver.find_element(*self.login_username_loc).clear()
#         self.driver.find_element(*self.login_username_loc).send_keys(uname)
#     def login_password(self,passwd):
#         #密码输入框
#         self.driver.find_element(*self.login_password_loc).clear()
#         self.driver.find_element(*self.login_password_loc).send_keys(passwd)
#     def logn_btn(self):
#         #登录按钮
#         self.driver.find_element(*self.login_button_loc).click()
#     def logun(self,username,password):
#         #登录操作
#         self.open()
#         self.login_username(username)
#         self.login_password(password)
#         self.logn_btn()
driver=webdriver.Chrome()



















