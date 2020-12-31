from selenium.webdriver.common.by import By
from page.base_page import BasePage


class CusumerPage(BasePage):
    getbeizhu_cusumer_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > span')
    transfer_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')

    def getbeizhu_cusumer(self):
        '''断言，线索转换客户以后，客户列表信息页面，对列表中的第一个客户名称定位'''
        self.find_element(self.getbeizhu_cusumer_locator)
        return self.find_element(self.getbeizhu_cusumer_locator)

    def savetransferclue(self):
        '''转换线索'''
        self.find_element(self.transfer_save_locator).click()
