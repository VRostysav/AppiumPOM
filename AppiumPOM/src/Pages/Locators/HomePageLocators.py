from appium.webdriver.common.appiumby import AppiumBy


class HomePageLocators:
    BURGER_MENU = (AppiumBy.XPATH, './/android.view.View[1]/android.widget.ImageView[1]')
    LOGOUT_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Logout"]')
    CONFIRMATION_LOGOUT_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Logout"]')

