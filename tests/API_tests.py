import json
import unittest
import requests
import utilities.custom_logger as cl
import logging

class LoginApiTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    def login(self, user, passwd):
        url = "http://media.cms.axtest.net/Login?"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain',
                   'RequestVerificationToken': 'FrxI5j-45Yfb8EFnvjssFmf4tC8WuazzyNJoprXwCpUzfZ67Et-cXBOdxzybV9IumvNgggVk8odgaM5VMm5cHeDjwruKrxukKs0CQxZO5gI1:YhYfmwMZIfjQ9o8A8PPFK9Jf0XQPypKfrZ-LRAj6tCmQxvzVu_yJQvp0F9Te5zFdLILVkVgTaN2YBSXu3uiIDEz-AmdSGfuD3epoPMbDg981'}
        r = requests.post(url, json.dumps({"userName": user,"password": passwd, }), headers=headers)
        print(r.status_code)
        print(r.json())
        return r

    def check_is_logged_in(self, r):
        return r.json()['IsLoggedIn']

    def test_valid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_valid_login started")
        self.log.info("*#" * 20)
        result=self.login("Test", "Candidate1")
        assert True== self.check_is_logged_in(result)

    def test_invalid_password(self):
        result = self.login("Test", "andidate1")
        assert False == self.check_is_logged_in(result)

    def test_invalid_username(self):
        result = self.login("est", "Candidate1")
        assert False == self.check_is_logged_in(result)

    def test_empty_password_API(self):
        result = self.login("Test", "nil")
        assert False == self.check_is_logged_in(result)

    def test_empty_username_API(self):
        result = self.login("nil", "Candidate1")
        assert False == self.check_is_logged_in(result)

    def test_empty_username_and_password_API(self):
        result = self.login("nil", "nil")
        assert False == self.check_is_logged_in(result)






