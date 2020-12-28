from selenium import webdriver  # 引入web浏览器
from time import sleep  # 引入时间库
from page import login_page  # 调用自己写的类
from page import home_page  # 调用自己写的类

driver = webdriver.Chrome()  # 选择浏览器
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(30)  # 设置等待时间
driver.get("http://localhost:8080/upload/admin")  # 打开网页
lp = login_page.LoginPage(driver)
# lp.open()    #打开页面
lp.input_uesrname("admin")  # 输入用户名
lp.input_password("admin123456")  # 输入密码
lp.sumbit()  # 点击按钮
sleep(3)
driver.switch_to.frame("header-frame")  # 定位到需要断言的那一栏
hp = home_page.Homepage(driver)
text = hp.get_username_text()  # 提取需要断言的目标文本

if text.strip() == '退出':  # 进行断言
    print("成功")
else:
    raise AssertionError("失败")
driver.quit()
