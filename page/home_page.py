from selenium.webdriver.common.by import By
from page.base_page import BasePage

class HomePage(BasePage):
    source_locator = (By.LINK_TEXT, '线索')
    cusumer_locator = (By.LINK_TEXT, '客户')

    def source(self):
        '''
        从home里面点击线索元素定位
        :return:
        '''
        self.find_element(self.source_locator).click()

    def cusumer(self):
        '''对导航列表中的客户元素定位'''
        self.find_element(self.cusumer_locator).click()

