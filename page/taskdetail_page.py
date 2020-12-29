from selenium.webdriver.common.by import By
from page.base_page import BasePage



class DetailTask(BasePage):
    alter_task_locator = (By.LINK_TEXT, '修改')

    get_detail_locator=(By.CSS_SELECTOR,'#tab1 > div.back_box > table > tbody > tr:nth-child(1) > td:nth-child(2)')

    def get_detail(self):
        '''断言查看成功，在任务详情中国获取到任务的主题文本'''
        self.find_element(self.get_detail_locator)
        return self.find_element(self.get_detail_locator)

    def alter_task(self):
        '''对进入任务详情页面中的修改元素定位'''
        self.find_element(self.alter_task_locator).click()

