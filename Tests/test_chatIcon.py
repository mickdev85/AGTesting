from selenium import webdriver

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_chatBox(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        homepage.chatBox().is_displayed()
        log.info("Chatbox is displayed")
        #self.driver.get_screenshot_as_file("ChatIcon.png")






