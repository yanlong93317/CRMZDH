from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
class MyTest_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/upload/admin")
        loc = (By.NAME, "username")
        pas = (By.NAME, "password")
        sub = (By.CSS_SELECTOR, "body > form > table > tbody > tr:nth-child(2)"
                                " > td > table > tbody > tr:nth-child(5) >"
                                " td:nth-child(2) > input")
        self.driver.find_element(*loc).send_keys("admin")
        self.driver.find_element(*pas).send_keys("admin123456")
        sleep(1)
        self.driver.find_element(*sub).click()
        self.driver.switch_to.frame("menu-frame")
        quan = self.driver.find_element(By.CSS_SELECTOR, "#menu-ul > li.collapse.lis.ico_8")
        sleep(1)
        quan.click()
        lieb = self.driver.find_element(By.CSS_SELECTOR,
                                        "#menu-ul > li.explode.lis.ico2_8 >"                                      " ul > li:nth-child(1) > a")
        lieb.click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("main-frame")
        tian = self.driver.find_element(By.CSS_SELECTOR, "body > h1 > span.action-span > a")
        sleep(1)
        tian.click()

    def test_register_cn(self):
        self.driver.find_element(By.NAME, "user_name").send_keys("long")
        self.driver.find_element(By.NAME, "email").send_keys("125676@qq.com")
        self.driver.find_element(By.NAME, "password").send_keys("admin123456")
        self.driver.find_element(By.NAME, "pwd_confirm").send_keys("admin123456")
        btn = self.driver.find_element(By.CSS_SELECTOR, "body > div.main-div > form > table > tbody > "
                                                        "tr:nth-child(5) > td >"
                                                        " input:nth-child(1)")
        sleep(2)
        btn.click()

    def test_register_zn(self):
        self.driver.find_element(By.NAME, "user_name").send_keys("张三")
        self.driver.find_element(By.NAME, "email").send_keys("125676@qq.com")
        self.driver.find_element(By.NAME, "password").send_keys("admin123456")
        self.driver.find_element(By.NAME, "pwd_confirm").send_keys("admin123456")
        btt = self.driver.find_element(By.CSS_SELECTOR, "body > div.main-div > form > table > tbody > "
                                                        "tr:nth-child(5) > td >"
                                                        " input:nth-child(1)")
        sleep(2)
        btt.click()

    def tearDown(self):
        print("清理")


if __name__ == "__main__":
    unittest.main()
