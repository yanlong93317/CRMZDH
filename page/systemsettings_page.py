from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep


class SystemSettings(BasePage):
    modulesettings_loc = (By.LINK_TEXT, '模块字段设置')
    addfield_loc = (By.CSS_SELECTOR, '#add')
    deletefield_loc = (
        By.CSS_SELECTOR, 'body > div.container > div.row > form > div:nth-child(1) > div > button:nth-child(1)')
    logoname_loc = (By.CSS_SELECTOR, '#name')
    enterprompt_loc = (By.CSS_SELECTOR, '#tips_td > td:nth-child(2) > input')
    savabutton_loc = (
        By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(16) > td:nth-child(2) > input.btn.btn-primary')
    tbody_loc = (By.CSS_SELECTOR, 'body > div.container > div.row > form > div:nth-child(2) > table > tbody')
    tbody2_loc = (By.CSS_SELECTOR, 'body > div.container > div.row > form > div:nth-child(2) > table > tbody')
    tr_loc = (By.TAG_NAME, 'tr')
    td_loc = (By.TAG_NAME, 'td')
    a_loc = (By.TAG_NAME, 'a')
    editfristsubmit_loc = (By.CSS_SELECTOR,
                           'body > div.container > div.row > form > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(5) > a.edit')
    editlogoname_loc = (By.CSS_SELECTOR, '#name')
    editsavabutton_loc = (
        By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(17) > td:nth-child(2) > input.btn.btn-primary')
    getfristkehuname_loc = (By.CSS_SELECTOR,
                            'body > div.container > div.row > form > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    listdispaly_loc = (By.CSS_SELECTOR,
                       'body > div.container > div.row > form > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(5) > a.indexShow')
    cancellistdispaly_loc = (By.CSS_SELECTOR,
                             'body > div.container > div.row > form > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(5) > a.indexShow')
    deletereault_loc = (By.CSS_SELECTOR, 'body > div.container > div.alert.alert-success')

    def modulesettings(self):
        '''
        点击系统设置下面的模块字段
        :return:
        '''
        self.find_element(self.modulesettings_loc).click()

    def addfield(self):
        '''
        添加字段
        :return:
        '''
        self.find_element(self.addfield_loc).click()

    def logoname(self, logoname):
        '''
        输入标识名
        :return:
        '''
        self.find_element(self.logoname_loc).send_keys(logoname)

    def enterprompt(self, prompt):
        '''
        定位到输入提示输入框
        :param prompt:
        :return:
        '''
        self.find_element(self.enterprompt_loc).send_keys()

    def savabutton(self):
        '''
        确认保存按钮
        :return:
        '''
        self.find_element(self.savabutton_loc).click()

    def addfieldset(self, logoname, enterprompt):
        '''
        添加字段集合
        :return:
        '''
        self.modulesettings()
        self.addfield()
        self.logoname(logoname)
        self.enterprompt(enterprompt)
        self.savabutton()

    def deletefield(self):
        '''
        删除按钮
        :return:
        '''
        self.find_element(self.deletefield_loc).click()

    def gettext(self, name):
        '''
        循环找出我想要的字段的名字
        :param name:
        :return:
        '''
        table_element = self.find_element(self.tbody_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        sleep(2)
        for tr in tr_lists:
            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            if td_list[1].text == name:
                print(td_list[1].text)
                return td_list[1]

    def editfristsubmit(self):
        '''
        第一行的编辑按钮
        :return:
        '''
        self.find_element(self.editfristsubmit_loc).click()

    def editlogoname(self, logoname):
        '''
        在客户名称里面输入数据
        :return:
        '''
        ele = self.find_element(self.editlogoname_loc)
        ele.clear()
        sleep(2)
        ele.send_keys(logoname)

    def editsavabutton(self):
        '''
        在点击确定按钮
        :return:
        '''
        self.find_element(self.editsavabutton_loc).click()

    def editlogonameset(self, logoname):
        '''
        编辑的操作的集合
        :return:
        '''
        self.editfristsubmit()
        self.editlogoname(logoname)
        self.editsavabutton()

    def getfristkehuname(self):
        '''
        返回第一行客户名称名字
        :return
        '''
        self.find_element(self.getfristkehuname_loc)
        return self.find_element(self.getfristkehuname_loc)

    def listdisply(self):
        '''
        列表显示的功能
        :return:
        '''
        self.find_element(self.listdispaly_loc).click()

    def cancellistdispaly(self):
        '''
        获取取消列表显示的的文本
        :return:
        '''
        self.find_element(self.cancellistdispaly_loc)
        return self.find_element(self.cancellistdispaly_loc)

    def locationlogoname(self,names):
        '''
        我要用for循环找出我们想要的字段，在点击删除
        :return:
        '''
        table_element = self.find_element(self.tbody2_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        sleep(2)
        for tr in tr_lists:
            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            print(td_list[1].text)
            if td_list[1].text == names:
                sleep(4)
                print(td_list[1].text)
                td_list[4].find_elements(*self.a_loc)[1].click()
                sleep(3)
                self.driver.switch_to.alert.accept()
                break

    def deletereault(self):
        '''
        获取删除后的文本提示内容
        :return:
        '''
        self.find_element(self.deletereault_loc)
        return self.find_element(self.deletereault_loc)
