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

#更多-站内信
more_locator=(By.LINK_TEXT,'更多')
driver.find_element(*more_locator).click()
sleep(1)
mail_locator=(By.LINK_TEXT,'站内信')
driver.find_element(*mail_locator).click()
sleep(1)
#1进入站内信列表信息页面，点击写信
writemail_locator=(By.LINK_TEXT,'写信')
driver.find_element(*writemail_locator).click()
sleep(1)
#进入写信页面，
#选择收件人为全部选择
shoujian_mail_locator=(By.CSS_SELECTOR,'#ta1 > input')
driver.find_element(*shoujian_mail_locator).click()
sleep(1)
#输入内容
content_mail_locator=(By.CSS_SELECTOR,'#dialog-message-send > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > textarea')
driver.find_element(*content_mail_locator).send_keys('要放元旦了')
sleep(2)
#点击发送
send_mail_locator=(By.CSS_SELECTOR,'#dialog-message-send > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
sleep(1)
driver.find_element(*send_mail_locator).click()
sleep(2)

#2查看站内信详细内容
see_mail_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
driver.find_element(*see_mail_locator).click()
sleep(1)

#3进入站内信详细内容后，点击回复，回复站内信
reply_mail_locator=(By.LINK_TEXT,'回复')
driver.find_element(*reply_mail_locator).click()
sleep(1)
#进入回复页面，输入内容
replycontent_mail_locator=(By.CSS_SELECTOR,'#dialog-send > form > table > tbody > tr > td:nth-child(2) > textarea')
driver.find_element(*replycontent_mail_locator).send_keys('知道了')     #输入回复内容
sleep(1)
#点击发送
replysend_mail_locator=(By.CSS_SELECTOR,'#dialog-send > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
driver.find_element(*replysend_mail_locator).click()
sleep(1)

#4.设置已读
#勾选主题前面的单选框
checkbox_mail_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
driver.find_element(*checkbox_mail_locator).click()
sleep(1)
#点击批量操作中的设置已读
piliang_mail_locator=(By.LINK_TEXT,'批量操作')
driver.find_element(*piliang_mail_locator).click()
sleep(1)
yidu_mail_locator=(By.LINK_TEXT,'设置已读')
driver.find_element(*yidu_mail_locator).click()
sleep(2)
#弹框确认设置已读
driver.switch_to.alert.accept()
sleep(3)

#5.删除
checkbox_mail_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
driver.find_element(*checkbox_mail_locator).click()
sleep(1)
#点击批量操作中的删除
piliang_mail_locator=(By.LINK_TEXT,'批量操作')
driver.find_element(*piliang_mail_locator).click()
sleep(1)
yidu_mail_locator=(By.LINK_TEXT,'删除')
driver.find_element(*yidu_mail_locator).click()
sleep(2)
#弹框确认设置已读
driver.switch_to.alert.accept()
sleep(3)

driver.quit()