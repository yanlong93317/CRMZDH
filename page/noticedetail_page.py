from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep



class DetailNotice(BasePage):
    title_notice_locator = (By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
    nrcontent_notice_locator = (By.CSS_SELECTOR, 'body')
    save_notice_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary')
    altercontent_notice_locator = (By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')



    def title_notice(self,btcontent):
        '''添加公告的详细页面中的标题元素定位'''
        ele=self.find_element(self.title_notice_locator)
        ele.clear()
        sleep(1)
        ele.send_keys(btcontent)

    def nrcontent_notice(self,nrcontent):
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('iframe')[0])
        #添加公告的详细页面中的内容元素定位
        ele=self.find_element(self.nrcontent_notice_locator)
        ele.clear()
        sleep(1)
        ele.send_keys(nrcontent)
        self.driver.switch_to.parent_frame()

    def save_notice(self):
        '''添加公告完成后保存元素定位'''
        self.find_element(self.save_notice_locator).click()

    def alterbiaoti_notice(self,alcontent):
        '''从详情页面中编辑按钮后进入编辑页面，对标题元素定位'''
        ele=self.find_element(self.altercontent_notice_locator)
        ele.clear()
        sleep(1)
        ele.send_keys(alcontent)


