from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep


class CusumerPage(BasePage):
    getbeizhu_cusumer_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6) > span')
    transfer_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')
    tansfer_kehu_locator=(By.CSS_SELECTOR,'#name')

    def getbeizhu_cusumer(self):
        '''断言，线索转换客户以后，客户列表信息页面，对列表中的第一个客户名称定位'''
        self.find_element(self.getbeizhu_cusumer_locator)
        return self.find_element(self.getbeizhu_cusumer_locator)

    def savetransferclue(self):
        '''转换线索'''
        self.find_element(self.transfer_save_locator).click()

    def tansfer_kehu(self,gsname):
        ele=self.find_element(self.tansfer_kehu_locator)
        ele.clear()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(1)
        ele.send_keys(gsname)
        sleep(2)

