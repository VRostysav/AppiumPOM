import pytest
from AppiumPOM.src.Pages.LoginPage import LoginPage
from AppiumPOM.src.Pages.HomePage import HomePage
import random


@pytest.mark.usefixtures('init_driver')
class TestSuccessfulLogInAndLogOut:
    @pytest.mark.tcid14
    def test_user_login_and_logout(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        login_page.click_login_button()
        login_page.click_agree_and_continue_button()
        login_page.enter_convo_number(2108094104)
        login_page.enter_convo_password('convorostyslav5')
        login_page.click_login_button_when_all_fields_are_filed()
        home_page.open_burger_menu()
        home_page.click_logout_button()
        home_page.click_confirmation_logout_button()
