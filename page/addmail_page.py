from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep

class AddMail(BasePage):
    writemail_locator = (By.LINK_TEXT, '写信')
    shoujian_mail_locator = (By.CSS_SELECTOR, '#ta1 > input')
    content_mail_locator = (By.CSS_SELECTOR, '#dialog-message-send > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > textarea')
    send_mail_locator = (By.CSS_SELECTOR, '#dialog-message-send > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
    getnr_mail_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    see_mail_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    inbox_mail_locator=(By.CSS_SELECTOR,'#t2')
    gerycontent_mail_locator=(By.CSS_SELECTOR,'#form2 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    checkbox_mail_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
    piliang_mail_locator = (By.LINK_TEXT, '批量操作')
    yidu_mail_locator = (By.LINK_TEXT, '设置已读')
    getyidu_mail_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')
    delete_mail_locator = (By.LINK_TEXT, '删除')
    getdelete_mail_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')

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
        sleep(3)
        self.shoujian_mail()
        sleep(3)
        self.content_mail(nrcontent)
        sleep(3)
        self.send_mail()
        sleep(1)

    def see_mail(self):
        '''对收件箱信息列表页面中的第一条内容元素定位'''
        self.find_element(self.see_mail_locator).click()

    def inbox_mail(self):
        '''写信页面中点击发件箱元素定位'''
        self.find_element(self.inbox_mail_locator).click()

    def gerycontent_mail(self):
        '''回复信息以后在收件箱中的第一条内容文本元素定位'''
        self.find_element(self.gerycontent_mail_locator)
        return self.find_element(self.gerycontent_mail_locator)

    def checkbox_mail(self):
        '''收件信息前的单选框元素定位'''
        self.find_element(self.checkbox_mail_locator).click()

    def piliang_mail(self):
        '''批量操作按钮元素定位'''
        self.find_element(self.piliang_mail_locator).click()

    def yidu_mail(self):
        '''批量操作下拉菜单中的设置已读元素操作'''
        self.find_element(self.yidu_mail_locator).click()
        self.driver.switch_to.alert.accept()

    def getyidu_mail(self):
        '''断言，设置已读后对设置已读成功文本元素定位'''
        self.find_element(self.getyidu_mail_locator)
        return self.find_element(self.getyidu_mail_locator)

    def delete_mail(self):
        '''批量操作下的删除元素定位'''
        self.find_element(self.delete_mail_locator).click()
        self.driver.switch_to.alert.accept()

    def getdelete_mail(self):
        '''断言，删除消息后的删除成功元素定位'''
        self.find_element(self.getdelete_mail_locator)
        return self.find_element(self.getdelete_mail_locator)


