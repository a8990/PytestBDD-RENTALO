from Config.config import testData
from Tests.test_base import BaseTest
from Pages.loginPage import LoginPage
import pytest

class   Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_crearcuenta_link_exist()
        assert flag


    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(testData.LOGIN_PAGE_TITLE)
        assert title ==  testData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(testData.USER_NAME, testData.PASSWORD)