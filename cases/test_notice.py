from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://192.168.1.211/crm/index.php?m=user&a=login')
driver.maximize_window()
driver.implicitly_wait(30)
sleep(1)
#登录
username_locator = (By.NAME, 'name')
password_locator = (By.NAME, 'password')
submit_locator = (By.CSS_SELECTOR, "input[value='登录']")
driver.find_element(*username_locator).send_keys('tangli')
sleep(1)
driver.find_element(*password_locator).send_keys('admin123456')
sleep(1)
driver.find_element(*submit_locator).click()
sleep(3)

#公告管理
#点击右上角的姓名
name_locator=(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a')
driver.find_element(*name_locator).click()
sleep(1)
#点击下拉菜单中的公告管理
notice_locator=(By.LINK_TEXT,'公告管理')
driver.find_element(*notice_locator).click()
sleep(1)

#1.新建公告
add_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(1) > div.pull-right > a')
driver.find_element(*add_notice_locator).click()
sleep(1)
#进入添加公告页面，在标题中输入内容
title_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
sleep(1)
driver.find_element(*title_notice_locator).send_keys('记得要考试了哦')
sleep(1)
#在内容中输入内容
content_notice_locator=(By.CSS_SELECTOR,'body')
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
sleep(1)
driver.find_element(*content_notice_locator).send_keys('考试')
sleep(1)
driver.switch_to.parent_frame()
sleep(1)
#点击保存,新建公告成功
save_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary')
sleep(1)
driver.find_element(*save_notice_locator).click()
sleep(2)

#2.查看公告的详细内容
see_notice_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
sleep(1)
driver.find_element(*see_notice_locator).click()
sleep(1)

#3.编辑修改公告
edit_notice_locator=(By.LINK_TEXT,'编辑')
sleep(1)
driver.find_element(*edit_notice_locator).click()
sleep(2)
#进入编辑页面，在内容输入框中输入内容
content_notice_locator=(By.CSS_SELECTOR,'body')
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
sleep(1)
driver.find_element(*content_notice_locator).send_keys('要记得大扫除哦')
sleep(1)
driver.switch_to.parent_frame()
sleep(1)
#点击保存
save_notice_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary')
sleep(1)
driver.find_element(*save_notice_locator).click()
sleep(2)

#4.点击停用
tingyong_notice_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')
driver.find_element(*tingyong_notice_locator).click()
sleep(1)

#5.删除公告
#选择某条公告前面的单选框，勾上
checkbox_notice_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
driver.find_element(*checkbox_notice_locator).click()
sleep(1)
#点击删除按钮
delete_notice_locator=(By.CSS_SELECTOR,'#delete')
driver.find_element(*delete_notice_locator).click()
sleep(1)
#弹框中确认删除
driver.switch_to.alert.accept()
sleep(3)


driver.quit()