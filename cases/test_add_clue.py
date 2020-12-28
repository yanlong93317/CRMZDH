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
#线索
#1添加线索
source_locator=(By.LINK_TEXT,'线索')
addsource_locator=(By.LINK_TEXT,'新建线索')
driver.find_element(*source_locator).click()
sleep(1)
driver.find_element(*addsource_locator).click()
sleep(1)
#负责人
fuzheren_locator=(By.ID,'owner_name')
driver.find_element(*fuzheren_locator).click()
sleep(1)
#负责人弹框表格搜索
chooseuser_locator=(By.ID,'d_name')
driver.find_element(*chooseuser_locator).send_keys('zhaijun')
sleep(1)
serch_locator=(By.CSS_SELECTOR,'#dialog-role-list > div > ul > button')
driver.find_element(*serch_locator).click()
sleep(1)
gouxuan_locator=(By.CSS_SELECTOR,'#d_content > tr > td:nth-child(1) > input[type=radio]')
driver.find_element(*gouxuan_locator).click()
sleep(1)
ok_locator=(By.CSS_SELECTOR,'body > div:nth-child(14) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')
driver.find_element(*ok_locator).click()
#公司
gongsi_locator=(By.CSS_SELECTOR,'#name')
driver.find_element(*gongsi_locator).send_keys('春晓')
sleep(1)
#来源
laiyuan_locator=(By.ID,'source')
locator=driver.find_element(*laiyuan_locator)
sleep(1)
select=Select(locator)
select.select_by_index(1)
sleep(1)
#联系人
lianxiren_locator=(By.ID,'contacts_name')
driver.find_element(*lianxiren_locator).send_keys('nichao')
sleep(1)
#备注
beizhu_locator=(By.ID,'description')
driver.find_element(*beizhu_locator).send_keys('唐丽添加线索测试')
sleep(1)
#保存
save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td > input:nth-child(1)')
driver.find_element(*save_locator).click()
sleep(3)

#2查看线索
#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(1)
#表格循环
tbody_locator=(By.CSS_SELECTOR,'#form1 > table > tbody')
tr_locator=(By.TAG_NAME,'tr')
td_locator=(By.TAG_NAME,'td')
tbody_elments=driver.find_element(*tbody_locator)
tr_list=tbody_elments.find_elements(*tr_locator)
for tr in tr_list:
    td_list=tr.find_elements(*td_locator)
    if td_list[1].text=='静夜思':
        td_list[11].find_element_by_css_selector('a:nth-child(1)').click()
        break
sleep(2)

#3修改线索
#直接在进入查看页面后进入到的线索详情页面中点击【修改】进行修改
alter_locator=(By.LINK_TEXT,'修改')
driver.find_element(*alter_locator).click()
sleep(1)
#点击修改后进入到编辑线索页面，在备注中输入内容：下次周六去
alter_beizhu_locator=(By.ID,'description')
driver.find_element(*alter_beizhu_locator).send_keys('下次周六去')
sleep(1)
#保存
alter_save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')
driver.find_element(*alter_save_locator).click()
sleep(1)

#4转换线索
#点击第一条线索后面的转换
transfer_clue_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(2)')
driver.find_element(*transfer_clue_locator).click()
sleep(2)

#保存
transfer_save_locator=(By.CSS_SELECTOR,'#form1 > table > tfoot > tr > td > input:nth-child(1)')
driver.find_element(*transfer_save_locator).click()
sleep(1)


#批量删除线索
#全选框勾选
deleteall_locator=(By.ID,'check_all')
driver.find_element(*deleteall_locator).click()
#点击批量操作下拉框中的删除
piliang_caozuo_locator=(By.LINK_TEXT,'批量操作')
driver.find_element(*piliang_caozuo_locator).click()
piliang_delete_locator=(By.LINK_TEXT,'批量删除')
driver.find_element(*piliang_delete_locator).click()
sleep(2)
#确定弹框删除
driver.switch_to.alert.accept()
sleep(2)


driver.quit()



