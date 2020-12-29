from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddTask(BasePage):
    addtask_locator=(By.LINK_TEXT,'新建任务')
    see_task_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(1)')
    getzhuangtai_task_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(6)')
    close_task_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(3)')
    getclose_task_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')
    gouxuan_task_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')    #点击第一个任务前面的单选框
    delete_task_locator = (By.ID, 'delete')
    getdelete_task_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')


    def addtask(self):
        '''
        从home里面点击线索元素后进入线索页面，对新建线索元素定位
        :return:
        '''
        self.find_element(self.addtask_locator).click()

    def see_task(self):
        '''查看线索'''
        self.find_element(self.see_task_locator).click()

    def getzhuangtai_task(self):
        '''修改任务的状态为进行中后，在任务列表的状态中获取进行中文本元素定位'''
        self.find_element(self.getzhuangtai_task_locator)
        return self.find_element(self.getzhuangtai_task_locator)

    def close_task(self):
        '''任务列表页面选中第一条后面的关闭元素定位'''
        self.find_element(self.close_task_locator).click()

    def getclose_task(self):
        '''断言，点击列表中的关闭后，提示关闭成功文本元素定位'''
        self.find_element(self.getclose_task_locator)
        return self.find_element(self.getclose_task_locator)

    def gouxuan_task(self):
        '''第一条任务前面的单选框元素定位'''
        self.find_element(self.gouxuan_task_locator).click()

    def delete_task(self):
        '''点击删除按钮元素定位'''
        self.find_element(self.delete_task_locator).click()
        self.driver.switch_to.alert.accept()

    def getdelete_task(self):
        '''断言，删除任务后对删除成功文本的元素定位'''
        self.find_element(self.getdelete_task_locator)
        return self.find_element(self.getdelete_task_locator)












