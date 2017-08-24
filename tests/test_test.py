from pages.login_page import LoginPage
from traceback import print_stack
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=1)
    def test_forgot_password(self):
        self.log.info("*#" * 20)
        self.log.info("test_forgot_password started")
        self.log.info("*#" * 20)
        self.lp.forgot_password()
        self.lp.email_me()


        print(element_text)
        self.lp.enter_username("Test")
        self.lp.email_me()







