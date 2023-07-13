from appium.webdriver.common.appiumby import AppiumBy


class LoginPageLocators:
    LOGIN_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log In"]')
    AGREEMENT_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Agree & Continue"]')
    CONVO_NUMBER_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[1]')
    CONVO_PASSWORD_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[2]')
    LOGIN_BUTTON_BEFORE_ACCOUNT_OPENING = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]')





