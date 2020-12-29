from selenium.webdriver.common.by import By
from page.base_page import BasePage

class EditTransfer(BasePage):
    transfer_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')

    def savetransfer(self):
        '''对在转化客户面中的保存元素定位'''
        self.find_element(self.transfer_save_locator).send_keys()

