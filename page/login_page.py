<<<<<<< HEAD
from selenium.webdriver.common.by import By     #引入By类
from page.base_page import BasePage             #调用自己写的类
from time import sleep     #引入时间


class LoginPage(BasePage):
    # 重写url属性，父类的url+/crm拼接
    _url = BasePage._url + "/crm"
    # 页面属性
    # 用户名输入框定位器
    username_locator = (By.NAME, "name")
    # 密码输入框定位器
    password_locator = (By.NAME, "password")
    # 登录按钮定位器
    submit_locator = (By.NAME, "submit")

    def input_uesrname(self, username):  # 定义一个类，用于找到用户名输入框并进行输入
        element = self.driver.find_element(*self.username_locator)
        element.clear()
        element.send_keys(username)
        sleep(2)  # 暂时2秒

    def input_password(self, password):  # 定义一个类，用于找到密码输入框并进行输入
        element = self.driver.find_element(*self.password_locator)
        element.clear()
        element.send_keys(password)
        sleep(3)

    def sumbit(self):  # 定义一个类，用于找到按钮并点击
        self.driver.find_element(*self.submit_locator).click()
        sleep(3)

    def login(self, username, passwrd):  # 定义一个类，用于进行登录的一些操作
        self.open()
        self.input_uesrname(username)
        self.input_password(passwrd)
        self.sumbit()
=======
# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:40
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : login_page.py
# @Project : CrmZDH.test
>>>>>>> 824be120d54df591256a117215688acdf4e4d7a7
