from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class BasicInformation(BasePage):
    basicInformationshopname_loc = (
    By.CSS_SELECTOR, '#tab1 > div.back_box.mar-top > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)')

    def basicInformationshopname(self):
        element=self.find_element(self.basicInformationshopname_loc)
        return element