import unittest
import time
from BeautifulReport import BeautifulReport
from config.config import REPORT_PATH, CASS_PATH

suite = unittest.defaultTestLoader.discover(CASS_PATH, "*_test.py")
now = time.strftime("%Y%m%d%H%M%S")
filename = "WkCrm-report-{}.html".format(now)
runner = BeautifulReport(suite)
runner.report(description="登录用例自动化测试",
              filename=filename,
              report_dir=REPORT_PATH)
