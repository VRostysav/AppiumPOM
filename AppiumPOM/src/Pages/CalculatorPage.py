from AppiumPOM.src.SeleniumExtended import SeleniumExtended
from AppiumPOM.src.Pages.Locators.CalculatorLocators import CalculatorPageLocators
import allure


class CalculatorPage(CalculatorPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Close instruction pop-up")
    def close_short_instruction(self):
        self.sl.wait_and_click(self.CLOSE_INSTRUCTION_BUTTON)

    @allure.step("Allow access to camera")
    def allow_access_to_camera(self):
        self.sl.wait_and_click(self.ALLOW_CAMERA)

    @allure.step("Select Calculation option in toolbar")
    def select_calculation_option(self):
        self.sl.wait_and_click(self.CALCULATION)

    @allure.step("Press the first number")
    def select_first_number(self):
        self.sl.wait_and_click(self.NUMBER_7)

    @allure.step("Click on '+' to add two numbers")
    def select_option_to_add(self):
        self.sl.wait_and_click(self.PLUS_BUTTON)

    @allure.step("Press second number")
    def select_second_number(self):
        self.sl.wait_and_click(self.NUMBER_3)



