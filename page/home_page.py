from selenium.webdriver.common.by import By
from page.base_page import BasePage

class HomePage(BasePage):
    source_locator = (By.LINK_TEXT, '线索')

    def source(self):
        '''
        从home里面点击线索元素定位
        :return:
        '''
        self.find_element(self.source_locator).click()

