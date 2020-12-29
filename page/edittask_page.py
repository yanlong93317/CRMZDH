from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.select import Select

class EditTask(BasePage):
    alter_wancheng_task_locator = (By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > select')  #状态进行中
    alter_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
    alter_save_task_locator = (By.XPATH, '/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')

    def alter_wancheng_task(self):
        '''对在编辑任务页面中的状态完成时改为进行中元素定位'''
        locator=self.find_element(self.alter_wancheng_task_locator)
        select = Select(locator)
        select.select_by_index(2)  # 赋值进行中

    def alter_save_task(self):
        '''对在编辑任务页面中的保存元素定位'''
        self.find_element(self.alter_save_task_locator).click()