import pytest
from AppiumPOM.src.Pages.CalculatorPage import CalculatorPage
import random


@pytest.mark.usefixtures('init_driver')
class TestAddOption:
    @pytest.mark.tcid13
    def test_option_of_adding_two_numbers(self):
        calculator_page = CalculatorPage(self.driver)

        calculator_page.close_short_instruction()
        calculator_page.allow_access_to_camera()
        calculator_page.select_calculation_option()
        calculator_page.select_first_number()
        calculator_page.select_option_to_add()
        calculator_page.select_second_number()


