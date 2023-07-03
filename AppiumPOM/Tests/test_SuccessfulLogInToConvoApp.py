import pytest
from AppiumPOM.src.Pages.LoginPage import LoginPage
import random


@pytest.mark.usefixtures('init_driver')
class TestSuccessfulLogIn:
    @pytest.mark.tcid14
    def test_user_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)

        login_page.click_login_button()
        login_page.click_agree_and_continue_button()
        login_page.enter_convo_number(2108094104)
        login_page.enter_convo_password('convorostyslav5')
        login_page.click_login_button_when_all_fields_are_filed()
