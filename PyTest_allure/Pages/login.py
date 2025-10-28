from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.actions = ActionChains(driver)

        # Locators
        self.username_field = (By.XPATH, "//input[@formcontrolname='username']")
        self.password_field = (By.XPATH, "//input[@formcontrolname='password']")
        self.sign_field = (By.XPATH, "//button[normalize-space(text())='Sign In']")
        self.re_login = (By.XPATH, "//span[normalize-space(text())='Logout']")

    # Actions
    def open_site(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_field)).click()

    def verify_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.re_login)).is_displayed()

