from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep

class EditClue(BasePage):
    alter_gs_locator = (By.ID, 'name')
    alter_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')

    def altergsclue(self,gsname):
        '''对在编辑线索页面中的备注元素定位'''
        ele=self.find_element(self.alter_gs_locator)
        ele.clear()
        self.driver.switch_to.alert.accept()
        sleep(4)
        ele.send_keys(gsname)

    def altersave(self):
        '''对在编辑线索页面中的保存元素定位'''
        self.find_element(self.alter_save_locator).click()