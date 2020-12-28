import unittest   #引入测试框架
from  HTMLTestReportCN import  HTMLTestRunner   #引入测试报告模板
dicv=unittest.defaultTestLoader.discover("./","test_login.py")  #找到需要打开的测试用例并设置为变量
f=open("./reult.html","wb")    #给报告命名
runner=HTMLTestRunner(stream=f,title="第一次自动化测试",
                      description="测试情况")   #实例化HTMLTestRunner
runner.run(dicv)    #开始执行
f.close()     #关闭文件


import time    #引入时间模块
import unittest   #引入测试框架
from BeautifulReport import BeautifulReport   #引入测试报告模板
dicv=unittest.defaultTestLoader.discover("./","test*.py")     #找到需要打开的测试用例并设置为变量
runner=BeautifulReport(dicv).report(description=u"测试情况",
                              filename=time.strftime("%Y-%m-%d %H_%M_%S"))   #实例化HTMLTestRunner