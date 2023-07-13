from AppiumPOM.src.SeleniumExtended import SeleniumExtended
from AppiumPOM.src.Pages.Locators.HomePageLocators import HomePageLocators
import allure


class HomePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Open burger menu")
    def open_burger_menu(self):
        self.sl.wait_and_click(self.BURGER_MENU)

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.sl.wait_and_click(self.LOGOUT_BUTTON)

    @allure.step("Click confirmation logout button")
    def click_confirmation_logout_button(self):
        self.sl.wait_and_click(self.CONFIRMATION_LOGOUT_BUTTON, timeout=8)
