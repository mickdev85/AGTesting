from selenium.webdriver.common.by import By

from pageObjects.deliveryPage import DeliveryPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    quantity = (By.XPATH, "//input[@class='input-text input-number']")

    addCart = (By.XPATH, "//div[@class='button-cart-container button-initial-add-container']")

    confirmCart = (By.XPATH, "//a[@href ='/shopping-cart']")

    popup = (By.XPATH, "//div[@class='frel_valign']/div/span")


    def getQuantity(self):
        return self.driver.find_element(*CheckoutPage.quantity)


    def getAddCart(self):
        return self.driver.find_element(*CheckoutPage.addCart)


    def getConfirmCart(self):
        self.driver.find_element(*CheckoutPage.confirmCart).click()
        deliverypage = DeliveryPage(self.driver)
        return deliverypage

    def getPopup(self):
        self.driver.find_element(*CheckoutPage.popup)









