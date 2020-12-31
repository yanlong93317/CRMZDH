from selenium.webdriver.common.by import By
from page.base_page import BasePage



class EditNotice(BasePage):
    getnrcontent_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > table > tbody > tr:nth-child(4) > td:nth-child(2)')
    edit_notice_locator = (By.LINK_TEXT, '编辑')



    def getnrcontent_notice(self):
        '''断言，查看后在通知详情页面中的内容文本元素定位'''
        self.find_element(self.getnrcontent_notice_locator)
        return self.find_element(self.getnrcontent_notice_locator)

    def edit_notice(self):
        '''对通知详情页面中的编辑按钮元素定位'''
        self.find_element(self.edit_notice_locator).click()









