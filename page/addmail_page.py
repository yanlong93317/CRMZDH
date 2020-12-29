from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddMail(BasePage):
    writemail_locator = (By.LINK_TEXT, '写信')
    shoujian_mail_locator = (By.CSS_SELECTOR, '#ta1 > input')
    content_mail_locator = (By.CSS_SELECTOR, '#dialog-message-send > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > textarea')
    send_mail_locator = (By.CSS_SELECTOR, '#dialog-message-send > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
    getnr_mail_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    see_mail_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    inbox_mail_locator=(By.LINK_TEXT,'收件箱')
    gerycontent_mail_locator=(By.CSS_SELECTOR,'#form2 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')

    def writemail(self):
        '''新建写信元素定位'''
        self.find_element(self.writemail_locator).click()

    def shoujian_mail(self):
        '''写信弹框页面中勾选全部定位'''
        self.find_element(self.shoujian_mail_locator).click()

    def content_mail(self,nrcontent):
        '''写信弹框页面中内容元素定位'''
        self.find_element(self.content_mail_locator).send_keys(nrcontent)

    def send_mail(self):
        '''写信弹框页面中发送按钮元素定位'''
        self.find_element(self.send_mail_locator).click()

    def getnr_mail(self):
        '''断言，写信成功后在收件列表页面第一个内容元素文本定位'''
        self.find_element(self.getnr_mail_locator)
        return self.find_element(self.getnr_mail_locator)

    def addmailjihe(self,nrcontent):
        '''写信集合'''
        self.writemail()
        self.shoujian_mail()
        self.content_mail(nrcontent)
        self.send_mail()

    def see_mail(self):
        '''对收件箱信息列表页面中的第一条内容元素定位'''
        self.find_element(self.see_mail_locator).click()

    def inbox_mail(self):
        '''写信页面中点击收件箱元素定位'''
        self.find_element(self.inbox_mail_locator).click()

    def gerycontent_mail(self):
        '''回复信息以后在收件箱中的第一条内容文本元素定位'''
        self.find_element(self.gerycontent_mail_locator)
        return self.find_element(self.gerycontent_mail_locator)


