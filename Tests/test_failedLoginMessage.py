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



class TestOne(BaseClass):

    def test_failedLogin(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        loginpage = homepage.registerButton()
        log.info("Entering incorrect username")
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

        errorMessage = loginpage.getError().text
        #self.driver.get_screenshot_as_file("FailedLogin.png")
        expectedError = "Sorry, this does not match our records. Check your spelling and try again."
        log.info("Text displayed is "+ errorMessage)
        assert errorMessage == expectedError

    @pytest.fixture(params=LoginData.test_LoginData)
    def getData(self, request):
        return request.param






