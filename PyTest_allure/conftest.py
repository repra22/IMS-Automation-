import allure
import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=f"Failure Screenshot - {request.node.name}",
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot if the test fails at the "call" stage
    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Failure Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )


