from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.select import Select
from time import sleep


class SaveTask(BasePage):
    zhuti_locator=(By.ID,'subject')
    task_fuzheren_locator = (By.ID, 'owner_name')  # 点击负责人输入框
    check_all_locator = (By.CSS_SELECTOR, '#ta1 > input')       #负责人弹框中勾全选
    ok_task_locator = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]/span')   #点击选择负责人保存
    miaosu_task_locator = (By.CSS_SELECTOR, 'body')    #描述
    save_task_locator = (By.CSS_SELECTOR,'body > div.container > div.row-fluid > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)')
    getzhuti_task_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(3) > a')



    def zhuti(self, ztcontent):
        '''添加任务中的主题的元素定位'''
        ele=self.find_element(self.zhuti_locator)
        ele.clear()
        sleep(1)
        ele.send_keys(ztcontent)

    def task_fuzheren(self):
        '''负责人定位，点击'''
        self.find_element(self.task_fuzheren_locator).click()

    def check_all(self):
        '''负责人弹框中勾选全部单选框运算定位'''
        self.find_element(self.check_all_locator).click()

    def ok_task(self):
        '''点击选择负责人保存元素定位'''
        self.find_element(self.ok_task_locator).click()

    def miaosu_task(self,mscontent):
        '''描述的元素定位'''
        ele=self.find_element(self.miaosu_task_locator)
        ele.clear()
        sleep(1)
        ele.send_keys(mscontent)

    def save_task(self):
        '''添加任务完成后保存元素定位'''
        self.find_element(self.save_task_locator).click()

    def getzhuti_task(self):
        '''断言，新增任务以后，在列表中第一个会有该任务主题元素定位'''
        self.find_element(self.getzhuti_task_locator)
        return self.find_element(self.getzhuti_task_locator)

    def savetaskjihe(self,ztcontent,mscontent):
        self.zhuti(ztcontent)
        self.task_fuzheren()
        self.check_all()
        self.ok_task()
        self.miaosu_task(mscontent)
        self.save_task()





