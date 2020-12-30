from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddNotice(BasePage):
    add_notice_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div.pull-right > a')
    getadd_notice_locator = (By.CSS_SELECTOR, 'body > div.container > div.alert.alert-success')
    see_notice_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    getalcontent_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')
    tingyong_notice_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')
    gettingyong_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')
    checkbox_notice_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
    delete_notice_locator = (By.CSS_SELECTOR, '#delete')
    serchcontent_notice_locator=(By.ID,'search')
    serch_notice_locator=(By.CSS_SELECTOR,'#searchForm > li:nth-child(4) > button')
    getdelete_notice_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td')


    def add_notice(self):
        '''添加公告元素定位'''
        self.find_element(self.add_notice_locator).click()

    def getadd_notice(self):
        '''断言，添加公告成功后的公告添加成功元素定位'''
        self.find_element(self.getadd_notice_locator)
        return self.find_element(self.getadd_notice_locator)

    def see_notice(self):
        '''对公告列表中的第一个公告标题元素定位进行查看'''
        self.find_element(self.see_notice_locator).click()

    def getalcontent_notice(self):
        '''修改标题以后跳转页面中获取公告保存成功元素定位'''
        self.find_element(self.getalcontent_notice_locator)
        return self.find_element(self.getalcontent_notice_locator)

    def tingyong_notice(self):
        '''公告列表页面中第一个公告点击停用的元素定位'''
        self.find_element(self.tingyong_notice_locator).click()

    def gettingyong_notice(self):
        '''断言，停用以后在获取当前提示的修改成功，已停用的文本元素定位'''
        self.find_element(self.gettingyong_notice_locator)
        return self.find_element(self.gettingyong_notice_locator)

    def checkbox_notice(self):
        '''选择第一条公告前面的单选框'''
        self.find_element(self.checkbox_notice_locator).click()

    def delete_notice(self):
        '''对删除按钮元素定位'''
        self.find_element(self.delete_notice_locator).click()
        self.driver.switch_to.alert.accept()

    def serchcontent_notice(self,sercontent):
        '''搜索框元素定位'''
        ele=self.find_element(self.serchcontent_notice_locator)
        ele.clear()
        ele.send_keys(sercontent)

    def serch_notice(self):
        '''搜索按钮元素定位'''
        self.find_element(self.serch_notice_locator).click()


    def getdelete_notice(self):
        '''断言，删除该公告后再搜索该公告提示暂无数据文本元素定位'''
        self.find_element(self.getdelete_notice_locator)
        return self.find_element(self.getdelete_notice_locator)













