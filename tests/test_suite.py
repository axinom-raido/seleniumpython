import os
import unittest
from datetime import datetime
import HTMLTestRunner

from tests.API_tests import LoginApiTests
from tests.login_tests import LoginTests
from tests.order_tests import OrderTests

#Get all tests from the test classes
tc1= unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2= unittest.TestLoader().loadTestsFromTestCase(LoginApiTests)
print("Gathered the tests for testing")

#Create a testsuite combining all test classes
smokeTest=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
print("Runing the testsuite")

""" HTML test runner needs some tweaking in order to work with Python 3.6.2
## File
dir = os.getcwd()
outfile = open(dir + "\SmokeTestReport_"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream = outfile, title ='Test Report', description ='Smoke Tests')
runner.run(smokeTest)
"""

