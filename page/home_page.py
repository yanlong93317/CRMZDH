from selenium.webdriver.common.by import By    #引入By类
from page.base_page import BasePage        #调用类

class Homepage():      #定义一个类
    _url=BasePage._url+"/crm/index.php?m=dynamic&a=index"     #设置url地址
    def __init__(self,driver,url=None):     #将类实例化
        self.driver=driver
        if not url:
            self.url=self._url
    username_locator=(By.CSS_SELECTOR,"body > div.navbar.navbar-"
                "inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                " ul:nth-child(1) > li:nth-child(1) > a")   #找寻一个目标，用于后面记那些具体操作

    def get_username_text(self):    #定义一个类
        return self.driver.find_element(*self.username_locator).text  #返回找到目标的文本