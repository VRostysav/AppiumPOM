from appium.webdriver.common.appiumby import AppiumBy


class CalculatorPageLocators:
    CLOSE_INSTRUCTION_BUTTON = (AppiumBy.ID, "calculator.scientific.math:id/close")
    ALLOW_CAMERA = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")
    CALCULATION = (AppiumBy.ID, "calculator.scientific.math:id/icon_calc")
    NUMBER_7 = (AppiumBy.ID, "calculator.scientific.math:id/kb_7")
    PLUS_BUTTON = (AppiumBy.ID, "calculator.scientific.math:id/kb_plus")
    NUMBER_3 = (AppiumBy.ID, "calculator.scientific.math:id/kb_3")
    EQUAL_BUTTON = (AppiumBy.ID, "calculator.scientific.math:id/kb_equal")
