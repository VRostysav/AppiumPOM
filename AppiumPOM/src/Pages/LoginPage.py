from AppiumPOM.src.SeleniumExtended import SeleniumExtended
from AppiumPOM.src.Pages.Locators.LoginPageLocators import LoginPageLocators
import allure


class LoginPage(LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Click Log in button")
    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    @allure.step("Click Agree&Continue button")
    def click_agree_and_continue_button(self):
        self.sl.wait_and_click(self.AGREEMENT_BUTTON)

    @allure.step("Enter convo number")
    def enter_convo_number(self, number):
        self.sl.wait_and_input_text(number, self.CONVO_NUMBER_FIELD)

    @allure.step("Enter convo password")
    def enter_convo_password(self, password):
        self.sl.wait_and_input_text(password, self.CONVO_PASSWORD_FIELD, password)

    @allure.step("Click Log in button one more time nad make share user is log in ")
    def click_login_button_when_all_fields_are_filed(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON_BEFORE_ACCOUNT_OPENING)

