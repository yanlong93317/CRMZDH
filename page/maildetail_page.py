from selenium.webdriver.common.by import By
from page.base_page import BasePage



class DetailMail(BasePage):

    getcontent_mail_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > pre')
    reply_mail_locator = (By.LINK_TEXT, '回复')
    replycontent_mail_locator = (By.CSS_SELECTOR, '#dialog-send > form > table > tbody > tr > td:nth-child(2) > textarea')
    replysend_mail_locator = (By.CSS_SELECTOR, '#dialog-send > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')


    def getcontent_mail(self):
        '''断言查看成功，在信息详情中获取到内容文本元素定位'''
        self.find_element(self.getcontent_mail_locator)
        return self.find_element(self.getcontent_mail_locator)

    def reply_mail(self):
        '''消息详情中对回复元素定位'''
        self.find_element(self.reply_mail_locator).click()

    def replycontent_mail(self,reeecontent):
        '''在回复弹框里面对内容元素定位'''
        self.find_element(self.replycontent_mail_locator).send_keys(reeecontent)


    def replysend_mail(self):
        '''在回复弹框里面对发送元素定位'''
        self.find_element(self.replysend_mail_locator).click()
