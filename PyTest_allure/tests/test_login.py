import pytest
import allure
from PyTest_allure.Pages.login import LoginPage

@allure.title("Login Test Using POM")
@allure.description("This test verifies that user can login successfully or captures a screenshot if login fails.")
def test_login(setup):
    driver = setup
    login = LoginPage(driver)

    with allure.step("Open login page"):
        login.open_site("https://redmiims.webredirect.himshang.com.np/")

    with allure.step("Enter username"):
        login.enter_username("Rishav")

    with allure.step("Enter password"):
        login.enter_password("wrongpassword")  # purposely wrong for demo

    with allure.step("Click Sign In"):
        login.click_sign_in()

    with allure.step("Verify login success"):
        assert login.verify_login() is True, "Login failed! Wrong credentials."


