from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.home_page import HomePage
class MyPanel(HomePage):
    '''我的面板'''
    # addpan_loc=(By.ID, "add")  # 添加组件
    # panname_loc=(By.ID, "title") #组件名
    # sure_loc=(By.NAME, "submit") #保存按钮
    # alter_loc=(By.ID, "update_widget")  # 修改按钮
    # elemint_loc=(By.NAME, "title") # 组件名输入框
    sched_loc=(By.CSS_SELECTOR, "#calendar > div.c-event-grid > div.c-event-body >"
                                         " div.data-head > a")  #日程
    schedule_loc=(By.NAME, "subject") #日程名
    sleep(2)
    make_loc=(By.NAME, "submit") #确定按钮
    # driver.find_element(By.NAME, "submit").click()

    # def addpanel(self):
    #     self.find_element(self.addpan_loc).click()
    #     sleep(2)
    # def inputpan(self,panel):
    #     self.find_element(self.panname_loc).send_keys(panel)
    #     sleep(3)
    # def djsure(self):
    #     self.find_element(self.sure_loc).click()
    #     sleep(2)
    # def addpan(self,pan):
    #     '''增加组件'''
    #     self.addpanel()
    #     self.inputpan(pan)
    #     self.djsure()
    # def alter(self):
    #     self.find_element(self.alter_loc).click()
    #     sleep(3)
    # def input_element(self,element):
    #     self.find_element(self.elemint_loc).clear()
    #     sleep(2)
    #     self.find_element(self.elemint_loc).send_keys(element)
    # def alter_ele(self,elename):
    #     '''修改组件名'''
    #     self.alter()
    #     self.input_element(elename)
    #     self.djsure()
    # def sched(self):
    #     self.find_element(self.sched_loc).click()
    #     sleep(2)
    # def schedule_input(self,schedule):
    #     self.find_element(self.schedule_loc).send_keys(schedule)
    #     sleep(2)
    # def make(self):
    #     self.find_element(self.make_loc).click()
    #     sleep(2)
    # def addschedule(self,schedule):
    #     self.sched()
    #     self.schedule_input(schedule)
    #     self.make()





