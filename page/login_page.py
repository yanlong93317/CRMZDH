from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class LoginPage(BasePage):
    # 用户名输入框定位器
    username_locator = (By.NAME, "name")
    # 密码输入框定位器
    password_locator = (By.NAME, "password")
    # 登录按钮定位器
    submit_locator = (
        By.CSS_SELECTOR, "body > div.container > div > div.span4 > div > form > fieldset > input.btn.btn-primary")

    def input_uesrname(self, username):  # 定义一个类，用于找到用户名输入框并进行输入
        element = self.find_element(self.username_locator)
        element.clear()
        element.send_keys(username)
        sleep(2)  # 暂时2秒

    def input_password(self, password):  # 定义一个类，用于找到密码输入框并进行输入
        element = self.find_element(self.password_locator)
        element.clear()
        element.send_keys(password)
        sleep(3)

    def sumbit(self):  # 定义一个类，用于找到按钮并点击
        self.find_element(self.submit_locator).click()
        sleep(3)



    def login(self, username, passwrod):  # 定义一个函数集合，用于进行登录的一些操作
        self.open()
        self.input_uesrname(username)
        self.input_password(passwrod)
        self.sumbit()
