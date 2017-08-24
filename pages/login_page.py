import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from selenium import webdriver
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _username_field = "input[type='text']"
    _password_field = "input[type='password']"
    _login_button = "//input[@value='Log in' and @type='button']"
    _password_forgotten_button= "//input[@value='Email me' and @type='button']"
    _password_forgotten_link = "Password forgotten?"
    _return_login_link= "Return to Login?"
    _error_locator = ".field-validation-error"


    #Methods

    def expected_error(self, expected_error_text, _error_locator):
        element = self.lp.getElement(self._error_locator, "css")
        element_text = element.get_attribute("innerHTML")
        if element_text == expected_error_text:
            return True
        else:
            return False
            print(element_text)

    def send_password(self, username):
        self.enter_username(username)
        self.email_me()

    def email_me(self):
        self.elementClick(self._password_forgotten_button, "xpath")


    def check_is_logged_in():
        return r.json()['IsLoggedIn']

    def enter_username(self, username):
        self.sendKeys(username, self._username_field,"css")

    def enter_password(self, password):
        self.sendKeys(password, self._password_field, "css")

    def click_login_button(self):
        self.elementClick(self._login_button, "xpath")

    def forgot_password(self):
        self.elementClick(self._password_forgotten_link, "link")



    def return_to_login(self):
        self.elementClick("Return to Login?", "link")

    def clear_fields(self):
        username_field = self.getElement(locator=self._username_field,locatorType='css')
        username_field.clear()
        password_field = self.getElement(locator=self._password_field,locatorType='css')
        password_field.clear()

    def login(self, username="", password=""):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result=self.lp.isElementPresent("#awe-homeButtonId", "css")
        return result
        print("Verify login successful")



    def verify_login_title(self):
        return self.verifyPageTitle("Axinom CMS")

    def verify_login_failed(self):
        result = self.isElementPresent(locator="//.field-validation-error[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def get_validation_errors(self, _error_text):
        element_list = self.driver.find_elements_by_class_name("field-validation-error")
        validation_error_list=[]
        for element in element_list:
            validation_error_list.append(element.text)
            self.log.info("*#" * 20)
            self.log.info("Validation errorslist: " + str(validation_error_list))
            self.log.info("*#" * 20)

        for error in validation_error_list:
            if _error_text in validation_error_list:
                return True
            else:
                return False


