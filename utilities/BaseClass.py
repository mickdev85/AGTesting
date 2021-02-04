import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\mickd\\PycharmProjects\\AmericanGolfTesting\\utilities\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger







####a kind of utility to allow you to use explicit wait a number of times across multiple tests
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 14).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[@value='Login']")))
