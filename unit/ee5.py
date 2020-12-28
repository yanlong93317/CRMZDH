import time
import unittest
from BeautifulReport import BeautifulReport

from unit import test_login
from unit import test_register

suite = unittest.TestSuite
suite.addTest(test_login("test_login_cn"))
suite.addTest(test_login("test_login_zn"))
suite.addTest(test_register("test_register_zn"))
suite.addTest(test_register("test_register_cn"))

runner=unittest.TextTestRunner()
runner.run(suite)



