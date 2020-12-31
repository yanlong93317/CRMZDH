from time import sleep
from selenium.webdriver.common.by import By
from page.home_page import HomePage


class MyPanel(HomePage):
    '''我的面板'''
    addpan_loc = (By.ID, "add")  # 添加组件
    panname_loc = (By.ID, "title")  # 组件名
    sure_loc = (By.NAME, "submit")  # 保存按钮
    alter_loc = (By.ID, "update_widget")  # 修改按钮
    elemint_loc = (By.NAME, "title")  # 组件名输入框
    sched_loc = (By.CSS_SELECTOR, "#calendar > div.c-event-grid > div.c-event-body >"
                                  " div.data-head > a")  # 日程
    schedule_loc = (By.NAME, "subject")  # 日程名
    make_loc = (By.NAME, "submit")  # 确定按钮
    notice_loc = (By.CSS_SELECTOR, "#widgets > div > "
                                   "div:nth-child(6) > div > div.dash-title > a")  # 公告列表
    bunsinsta_loc = (By.CSS_SELECTOR, "#widgets > div > div.sort-list.ui-sortable >"
                                      " div:nth-child(1) > div > div.dash-title > a")  # 商机统计
    alterzjm_loc=(By.CSS_SELECTOR,"#widgets > div > div.sort-list.ui-sortable >"
                        " div:nth-child(1) > div > div.dash-title") #组件名修改
    sche_loc=(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a")
    notice_locator=(By.CSS_SELECTOR, "body > div.container > div.row >"
                                    " div:nth-child(1) > div.pull-right > a") #公告
    shopstatic_loc= (By.ID, "show_report") #商机统计
    moudu_loc=(By.CSS_SELECTOR, "#widgets > div > div.sort-list.ui-sortable")


    def addpanel(self):
        self.find_element(self.addpan_loc).click()
        sleep(1)

    def inputpan(self, panel):
        self.find_element(self.panname_loc).send_keys(panel)
        sleep(1)

    def djsure(self):
        self.find_element(self.sure_loc).click()
        sleep(1)
    def mouduss(self):
        mouduss=self.find_element(self.moudu_loc)
        moudu = mouduss.find_elements(By.CLASS_NAME,"dash-title")
        return moudu[-1].text
    def addpan(self, pan):
        '''增加组件'''
        self.addpanel()
        self.inputpan(pan)
        self.djsure()

    def alter(self):
        self.find_element(self.alter_loc).click()
        sleep(1)

    def input_element(self, element):
        self.find_element(self.elemint_loc).clear()
        sleep(1)
        self.find_element(self.elemint_loc).send_keys(element)
    def alterzjm(self):
        ele=self.find_element(self.alterzjm_loc).text
        return ele

    def alter_ele(self, elename):
        '''修改组件名'''
        self.alter()
        self.input_element(elename)
        self.djsure()

    def sched(self):
        self.find_element(self.sched_loc).click()
        sleep(1)

    def schedule_input(self, schedule):
        self.find_element(self.schedule_loc).send_keys(schedule)
        sleep(1)

    def make(self):
        self.find_element(self.make_loc).click()
        sleep(1)
    def seche(self):
        sche=self.find_element(self.sche_loc).text
        return sche


    def addschedule(self, schedule):
        '''增加日程'''
        self.sched()
        self.schedule_input(schedule)
        self.make()
    def sche(self):
        sched=self.find_element(self.notice_locator).text.strip()
        return sched
    def notice(self):
        '''公告'''
        self.find_element(self.notice_loc).click()
        sleep(1)


    def bunsinsta(self):
        '''商机统计'''
        self.find_element(self.bunsinsta_loc).click()
        sleep(1)
    def shopstatic(self):
        shopstic=self.find_element(self.shopstatic_loc).text.strip()
        return shopstic

