from selenium.webdriver.common.by import By
from page.base_page import BasePage



class ClueXiangQing(BasePage):
    alter_locator = (By.LINK_TEXT, '修改')

    def alterclue(self):
        '''对进入线索详情页面中的修改元素定位'''
        self.find_element(self.alter_locator).click()