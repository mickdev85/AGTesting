import time

from py._log import log
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import checkoutPage
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.deliveryPage import DeliveryPage
from utilities.BaseClass import BaseClass


class TestFour(BaseClass):
    def test_freeDelivery(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getSearchBar().send_keys("callaway golf balls")
        time.sleep(3)
        balls = homepage.getCallawayBalls()
        # balls = self.driver.find_elements_by_xpath("//div[@class='name']")
        # print(len(balls))
        for ball in balls:
            if ball.text == "Callaway Warbird Plus 12 Ball Pack":
                ball.click()
                break

        checkoutpage = CheckoutPage(self.driver)
        chooseQuantity = checkoutpage.getQuantity()
        action = ActionChains(self.driver)
        action.double_click(chooseQuantity).perform()
        action.double_click(chooseQuantity).perform()
        chooseQuantity.send_keys("10")
        self.driver.implicitly_wait(5)

        try:
            popup = checkoutpage.getPopup()
            if popup.is_displayed():
                popup.click()

        except Exception as e:
            print(e)
        checkoutpage.getAddCart().click()
        deliverypage = checkoutpage.getConfirmCart()     #trigger point
        #self.driver.get_screenshot_as_file("FreeDelivery.png")
        subtotal = deliverypage.getTotalAmount().text[1:]
        log.info("Total amount of purchase is" + subtotal)
        deliveryAmount = deliverypage.getDeliveryCost().text[1:]
        log.info("Delivery amount is" + deliveryAmount)

        if float(subtotal) > 50:
            assert float(deliveryAmount) == 0
            print('amount is greater than 50 and 0 delivery fees is verified')
        else:
            print('amount is less then 50, so delivery fees is {}'.format(float(deliveryAmount)))

        log.info("Offer is working")

