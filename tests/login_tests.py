from pages.login_page import LoginPage
from traceback import print_stack
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def object_setup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=1)
    def test_t1_valid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1_valid_login started")
        self.log.info("*#" * 20)
        self.lp.login("Test", "Candidate1")

        #basic assertion for being logged in
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title Verification")
        result2=self.lp.isElementPresent("#awe-homeButtonId","css")
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t1_valid_login", result2, "Login Verification")



    @pytest.mark.run(order=2)
    def test_t2_missing_username(self):
        _error_text = "The User name field is required."
        self.log.info("*#" * 20)
        self.log.info("test_t2_missing_username started")
        self.log.info("*#" * 20)
        self.lp.login("", "Candidate1")
        result=self.lp.get_validation_errors(_error_text)
        #assert result ==True



    @pytest.mark.run(order=3)
    def test_t3_missing_password(self):
        _error_text = "The Password field is required."
        self.log.info("*#" * 20)
        self.log.info("test_t2_missing_password started")
        self.log.info("*#" * 20)
        self.lp.login("Test", "")
        result = self.lp.get_validation_errors(_error_text)
        print("Result: " + str(result))
        #assert result == True

    @pytest.mark.run(order=4)
    def test_t4_missing_username_and_password(self):
        self.log.info("*#" * 20)
        self.log.info("test_t4_missing_username_and_password started")
        self.log.info("*#" * 20)
        self.lp.login("", "")
        result = self.lp.get_validation_errors(_error_text)
        print("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=5)
    def test_t5_invalid_password(self):
        self.log.info("*#" * 20)
        self.log.info("test_t5_invalid_password started")
        self.log.info("*#" * 20)
        self.lp.login("Test", "Candidate2")
        result=self.lp.verify_login_failed()
        assert result== True

    @pytest.mark.run(order=6)
    def test_t5_invalid_username(self):
        self.log.info("*#" * 20)
        self.log.info("test_t5_invalid_username started")
        self.log.info("*#" * 20)
        self.lp.login("Test1", "Candidate1")
        self.lp.verify_login_failed()