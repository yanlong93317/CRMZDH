from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# # 打开登录网页
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)

#添加组件
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)




driver.find_element(By.ID,"add").click() #点击添加组件
sleep(2)
driver.find_element(By.ID,"title").send_keys("红红火火")
sleep(2)
driver.find_element(By.NAME,"submit").click()
sleep(6)

ds=driver.find_element(By.CSS_SELECTOR,"#widgets > div > div.sort-list.ui-sortable")
td=ds.find_elements(By.CLASS_NAME,"dash-title")

print(td[-1].text)


#
# dd=driver.find_element(By.CSS_SELECTOR,"body > div.container > "
#                         "div.alert.alert-success").text
# print(dd)
# if "添加组件成功" in dd:
#     print("成功")
# else:
#     raise AssertionError("失败")



# driver.quit()
# driver=webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# #登录
# driver.find_element(By.NAME,"name" ).send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME,"password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME,"submit").click()
# sleep(2)
# #组件修改
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
#                                     "> div.nav-collapse.collapse > ul.nav.pull-right > "
#                                     "li:nth-child(6) > a > img").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
#                                     " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
# sleep(2)
# driver.find_element(By.ID,"update_widget").click()  #点击修改按钮
# sleep(2)
# driver.find_element(By.NAME,"title").clear()  #清空
# driver.find_element(By.NAME,"title").send_keys("hello")
# sleep(2)
# driver.find_element(By.NAME,"submit").click()
# # sleep(5)
# # # driver.quit()
# # # driver=webdriver.Chrome()
# # # driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # #登录
# # driver.find_element(By.NAME,"name" ).send_keys("huachuan")
# # sleep(1)
# driver.find_element(By.NAME,"password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME,"submit").click()
# sleep(2)
# 添加日程
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
#                                     "> div.nav-collapse.collapse > ul.nav.pull-right > "
#                                     "li:nth-child(6) > a > img").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
#                                     " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"#calendar > div.c-event-grid > div.c-event-body >"
#                                     " div.data-head > a").click()
# sleep(2)
# driver.find_element(By.NAME,"subject").send_keys("胜任")
# sleep(2)
# driver.find_element(By.NAME,"submit").click()
#
# sleep(5)
# driver.quit()
# driver=webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# #登录
# driver.find_element(By.NAME,"name" ).send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME,"password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME,"submit").click()
# sleep(2)
# # 切换到公告列表
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
#                                     "> div.nav-collapse.collapse > ul.nav.pull-right > "
#                                     "li:nth-child(6) > a > img").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
#                                     " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
# sleep(2)
#
# driver.find_element(By.CSS_SELECTOR,"#widgets > div > div:nth-child(6) > div > div.dash-title > a").click()
# sleep(5)
# ss=driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row >"
#                                     " div:nth-child(1) > div.pull-right > a").text
# ss1=ss.strip()
# if "添加公告"==ss1:
#     print("成功")
# else:
#     raise AssertionError("失败")
# # driver.quit()
# driver=webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # 登录
# driver.find_element(By.NAME,"name" ).send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME,"password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME,"submit").click()
# sleep(2)
# # 商机统计
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
#                                     "> div.nav-collapse.collapse > ul.nav.pull-right > "
#                                     "li:nth-child(6) > a > img").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
#                                     " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
# sleep(2)
#
#
# driver.find_element(By.CSS_SELECTOR,"#widgets > div > div.sort-list.ui-sortable >"
#                                     " div:nth-child(1) > div > div.dash-title > a").click()
#
# ds=driver.find_element(By.ID,"show_report").text
# print(ds)
#
# ss1=ds.strip()
# if "商机统计报表"==ss1:
#     print("成功")
# else:
#     raise AssertionError("失败")
# driver.quit()
# sleep(5)
# driver.quit()






