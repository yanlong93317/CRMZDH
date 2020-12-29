from selenium.webdriver.common.by import By
from page.base_page import BasePage

class EditClue(BasePage):
    alter_beizhu_locator = (By.ID, 'description')
    alter_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')

    def alterclue(self):
        '''对在编辑线索页面中的备注元素定位'''
        self.find_element(self.alter_beizhu_locator).send_keys()

    def altersave(self):
        '''对在编辑线索页面中的保存元素定位'''
        self.find_element(self.alter_save_locator).click()