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

#1.任务
#添加任务
#任务定位，点击
task_locator=(By.LINK_TEXT,'任务')
driver.find_element(*task_locator).click()
sleep(1)
#新建任务，点击
addtask_locator=(By.LINK_TEXT,'新建任务')
driver.find_element(*addtask_locator).click()
sleep(1)
#进入添加任务页面，输入主题，负责人，描述
zhuti_locator=(By.ID,'subject')
driver.find_element(*zhuti_locator).send_keys('31号大扫除')    #主题
sleep(1)
task_fuzheren_locator=(By.ID,'owner_name')           #点击负责人输入框
driver.find_element(*task_fuzheren_locator).click()
sleep(1)
check_all_locator=(By.CSS_SELECTOR,'#ta1 > input')
driver.find_element(*check_all_locator).click()       #负责人弹框中勾全选
sleep(1)
ok_task_locator=(By.XPATH,'/html/body/div[7]/div[3]/div/button[1]/span')
driver.find_element(*ok_task_locator).click()         #点击选择负责人保存
sleep(1)
miaosu_task_locator=(By.CSS_SELECTOR,'body')
driver.find_element(*miaosu_task_locator).send_keys('添加任务唐丽测试1')      #描述
sleep(1)
save_task_locator=(By.CSS_SELECTOR,'body > div.container > div.row-fluid > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)')
driver.find_element(*save_task_locator).click()     #点击添加内容保存
sleep(1)


#2查看任务
#任务列表信息页面中定位第一个主题进行点击后面的查看
see_task_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(1)')
driver.find_element(*see_task_locator).click()
sleep(1)


#3修改任务
alter_task_locator=(By.LINK_TEXT,'修改')
sleep(1)
driver.find_element(*alter_task_locator).click()       #点击任务详情中的修改
sleep(1)
#进入修改页面，修改状态为进行中
alter_wancheng_task_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > select')
locator=driver.find_element(*alter_wancheng_task_locator)
sleep(1)
select=Select(locator)
select.select_by_index(2)     #赋值进行中
sleep(1)
alter_save_task_locator=(By.XPATH,'/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')
driver.find_element(*alter_save_task_locator).click()      #点击任务修改中的保存按钮
sleep(2)
#点击关闭
close_task_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(3)')
driver.find_element(*close_task_locator).click()
sleep(2)
#删除任务
gouxuan_task_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > input')
sleep(1)
driver.find_element(*gouxuan_task_locator).click()    #点击第一个任务前面的单选框
sleep(5)
delete_task_locator=(By.ID,'delete')
driver.find_element(*delete_task_locator).click()     #点击删除按钮
sleep(3)
driver.switch_to.alert.accept()     #弹框中确定删除
sleep(3)

driver.quit()




