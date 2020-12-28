from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from UNIT import login_date
from UNIT import logincsv
class MyTest_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/upload/admin")

    def test_login_cn(self):
        # username,password,locator= login_date.read_excel()[1]
        username, password, locator =logincsv.read_csv()[1]
        loc = (By.NAME, "username")
        pas = (By.NAME, "password")
        sub = (By.CSS_SELECTOR, "input[value='进入管理中心']")
        self.driver.find_element(*loc).send_keys(username)
        self.driver.find_element(*pas).send_keys(password)
        sleep(2)
        self.driver.find_element(*sub).click()
        ul=self.driver.current_url
        self.assertIn(ul,locator)
        sleep(5)
        self.driver.quit()
    @unittest.skip("跳过")
    def test_login_zn(self):
        loc = (By.NAME, "username")
        pas = (By.NAME, "password")
        sub = (By.CSS_SELECTOR, "body > form > table > tbody > tr:nth-child(2)"
                                " > td > table > tbody > tr:nth-child(5) >"
                                " td:nth-child(2) > input")
        self.driver.find_element(*loc).send_keys("张三")
        self.driver.find_element(*pas).send_keys("admin123456")
        sleep(2)
        self.driver.find_element(*sub).click()
        sleep(3)
    def tearDown(self):
            print("清理")

if __name__=="__main__":
    unittest.main()
