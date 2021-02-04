import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from testData.LoginData import LoginData
from utilities.BaseClass import BaseClass



class TestTwo(BaseClass):

    def test_successfulLogin(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        loginpage = homepage.registerButton()
        log.info("username is " + getData["username"])
        loginpage.getUsername().send_keys(getData["username"])
        loginpage.getPassword().send_keys(getData["password"])
        try:
            popup = loginpage.getPopup()
            if popup.is_displayed():
                popup.click()

        except Exception as e:
            print(e)
        self.verifyLinkPresence("//button[@value='Login']")
        loginpage.loginButton().click()
        #self.driver.get_screenshot_as_file("SuccessLogin.png")
        successMessage = loginpage.getSuccess().text
        expectedMessage = "Welcome Michael"
        log.info("message displayed is " + successMessage)

        assert successMessage == expectedMessage

    @pytest.fixture(params=LoginData.test_LoginData1)
    def getData(self, request):
        return request.param

