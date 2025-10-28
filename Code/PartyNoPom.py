import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys

from PartyPom import PartyLed

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://redmiims.webredirect.himshang.com.np/#/login")  # Replace with your login page URL

login = PartyLed(driver)
login.enter_username("Rishav")  # Replace "admin" with your username
login.enter_password("Ims@1234")
login.enter_sign_in()
try:
    login.entered_login()
except (TimeoutException, NoSuchElementException):
    print("Login Not seen")

#login.entered_login()
time.sleep(5)
login.enter_sign_in()
login.account_clicked()
time.sleep(20)
login.switch_to_new_window()

login.account_transaction_click()

time.sleep(20)

login.opening_entry_click()
time.sleep(10)

time.sleep(10)
login.Ledger_enter()

login.add_amount_dr("50")
time.sleep(10)

login.save_click()

time.sleep(20)

login.close_me()

time.sleep(10)

login.edit_click()
time.sleep(10)
login.selecting_edit()
time.sleep(20)


driver.quit()
