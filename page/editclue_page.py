from selenium.webdriver.common.by import By
from page.base_page import BasePage

class EditClue(BasePage):
    alter_gs_locator = (By.ID, 'name')
    alter_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')

    def altergsclue(self,gsname):
        '''对在编辑线索页面中的备注元素定位'''
        self.find_element(self.alter_gs_locator).send_keys(gsname)

    def altersave(self):
        '''对在编辑线索页面中的保存元素定位'''
        self.find_element(self.alter_save_locator).click()