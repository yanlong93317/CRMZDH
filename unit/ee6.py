
import unittest
from  HTMLTestReportCN import  HTMLTestRunner
dicv=unittest.defaultTestLoader.discover("./","ee5.py")
f=open("./reult.html","wb")
runner=HTMLTestRunner(stream=f,title="第一次自动化测试",
                      description="测试情况")
runner.run(dicv)
f.close()