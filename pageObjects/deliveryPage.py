from selenium.webdriver.common.by import By


class DeliveryPage:
    def __init__(self, driver):
        self.driver = driver

    totalAmount = (By.XPATH, "//tr[@class='order-subtotal']/td[2]")

    deliveryCost = (By.XPATH, "//tr[@class='order-shipping']/td[2]")

    def getTotalAmount(self):
        return self.driver.find_element(*DeliveryPage.totalAmount)

    def getDeliveryCost(self):
        return self.driver.find_element(*DeliveryPage.deliveryCost)
