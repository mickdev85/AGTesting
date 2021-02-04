from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    register = (By.LINK_TEXT, "My Account / Register")

    chat = (By.CSS_SELECTOR, "button.chat-icon")

    # cookie = (By.XPATH, "//button[contains(text(),'Accept')]")

    searchBar = (By.XPATH, "//input[@id='q']")

    callawayBalls = (By.XPATH, "//div[@class='name']")

    def registerButton(self):
        self.driver.find_element(*HomePage.register).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def chatBox(self):
        return self.driver.find_element(*HomePage.chat)

    # def cookieBanner(self):
    #    return self.driver.find_element(*HomePage.cookie)

    def getSearchBar(self):
        return self.driver.find_element(*HomePage.searchBar)

    def getCallawayBalls(self):
        return self.driver.find_elements(*HomePage.callawayBalls)




