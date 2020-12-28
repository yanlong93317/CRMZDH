from selenium.webdriver.common.by import By
class LoginPage():
    _url="http://localhost:8080/upload/admin"
    def __init__(self,driver,url=None):
        self.driver=driver
        if not url:
            self.url=self._url

    username_localtor=(By.NAME,'username')
    #密码输入框定位器
    passwprd_locaktor=(By.NAME,'password')
    #登录按钮定位器
    submit_localtor=(By.CSS_SELECTOR,"input[value='进入管理中心']")
    #页面操作
    def input_username(self,username):  #定义一个用户名函数并进行输入
        self.driver.find_element(*self.username_localtor).send_keys(username)
    def input_password(self,password):  #定义一个密码函数并进行输入
        self.driver.find_element(*self.passwprd_locaktor).send_keys(password)
    def submit(self):  #定义一个按钮函数并进行点击
        self.driver.find_element(*self.submit_localtor).click()
    def open(self,url):    #打开网页
        self.driver.get(url)