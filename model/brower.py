# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:06
# @Author : yanlong
# @Email : tangli@tmail.com
# @File : brower.py
# @Project : ZDH

from selenium import webdriver
def chrome():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver
def firefox():
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver
def ie():
    driver=webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver
def opera():
    driver=webdriver.Opera()
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver
