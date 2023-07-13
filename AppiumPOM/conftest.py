import pytest
from appium import webdriver
import os
import allure

"""
 Якщо захочеш ранити тести не паралельно то залиш в params тільки якесь одне значення.
 
 Щоб заранити тести потірбно заранити наступну команду(таким чином воно заранить всі тести по поряду): pytest Щоб 
 заранити тести в паралель : pytest -n2 (значення білья n відповідаж за кількість потоків) 
 Щоб заранити тести і отримати репорт потрібно по порядку заранити дві команди :
  1) pytest --alluredir="C:/Users/Family/AppiumPOM/AppiumPOM/Allure-Results"  - в твому випдку шлях буде інший
  2) allure serve "C:/Users/Family/AppiumPOM/AppiumPOM/Allure-Results"   - - в твому випдку шлях буде інший
 Якщо хочеш отримати репорт і ранити тести в паралель то потірбно до команди 1) в кінці додати -n 2
 
 
 APPIUM INSPECTOR and APPIUM
 
 для того щоб подивитися udid девайсу в консолі потрібно ввест: adb devices
 для того щоб стартанути appium потрібно ввести команду appium -p порт
 (відповідно значення порта потрібно змінити в змінній driver)
 
 
 
 """


@pytest.fixture(params=["Pixel 5 + Android 12"], scope="class")
def init_driver(request):
    if request.param == "Pixel 5 + Android 12":
        options = {
            "appium:platformName": "Android",
            "appium:platformVersion": "12",
            "appium:deviceName": "Pixel 5",
            "appium:udid": "emulator-5554",
            "appium:app": r"C:\Users\Family\AppiumPOM\AppiumPOM\AppBinaries\ConvoBeta-1.4.0.apk",
            "appium:automationName": "UiAutomator2",
            "appium:autoGrantPermissions": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4724", options)
    # if request.param == "Pixel 6 + Android 13":
    #     options = {
    #         "appium:platformName": "Android",
    #         "appium:platformVersion": "13",
    #         "appium:deviceName": "Pixel 6 Pro",
    #         "appium:udid": "emulator-5554",
    #
    #         # Лінка на тестову апку(шлях зміниш на той якиий тобі підійде).
    #         #"appium:app": r"C:\Users\Family\AppiumPOM\AppiumPOM\AppBinaries\Calculator.apk",
    #
    #         # Якщо потірбно використовувати конво апку а не тестову
    #          "appium:app": r"C:\Users\Family\AppiumPOM\AppiumPOM\AppBinaries\ConvoBeta-1.4.0.apk",
    #
    #         "appium:automationName": "UiAutomator2",
    #         "appium:autoGrantPermissions": "true"
    #     }
    #     driver = webdriver.Remote("http://127.0.0.1:4724", options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = "C:/Users/Family/AppiumPOM/AppiumPOM/Allure-Results"
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set")
                screenshot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs["request"]
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
