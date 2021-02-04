from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@id='dwfrm_login_username']")
    password = (By.XPATH, "//input[@id='dwfrm_login_password']")
    login = (By.XPATH, "//button[@value='Login']")
    error = (By.XPATH, "//div[@class='error-form']")
    success = (By.XPATH, "//span[contains(text(),'Welcome Michael')]")
    popup = (By.XPATH, "//div[@class='frel_valign']/div/span")


    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)


    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.login)

    def getError(self):
        return self.driver.find_element(*LoginPage.error)

    def getSuccess(self):
        return self.driver.find_element(*LoginPage.success)

    def getPopup(self):
        return self.driver.find_element(*LoginPage.popup)


