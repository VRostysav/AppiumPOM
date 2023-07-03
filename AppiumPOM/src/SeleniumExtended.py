import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 5

    def wait_and_input_text(self, text, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
