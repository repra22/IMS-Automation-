from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class PomLogin:
    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.actions = ActionChains(self.driver)


        # Locators
        self.username_field =(By.XPATH,"//input[@formcontrolname='username']")
        self.password_field =(By.XPATH,"//input[@formcontrolname='password']")
        self.sign_field =(By.XPATH,"//button[normalize-space(text())='Sign In']")
        self.re_login = (By.XPATH,"//span[normalize-space(text())='Logout']")
        self.account_click = (By.XPATH , "//span[text()='Accounting Module']")
        self.account_Transaction = (By.XPATH , "//span[normalize-space(text())='Transactions']")
        self.opening_entries = (By.XPATH ,"//a[@title='Opening Entries']")
        self.ledger=(By.ID,"ACCODEInput_0")
        self.dr_amount =(By.XPATH,"//input[@id='DrAmtInput_0']")
        self.save_button=(By.XPATH,"//button[normalize-space(text())='F6 SAVE']")
        self.close_button = (By.XPATH,"//button[normalize-space(text())='No']")
        self.edits = (By.XPATH , "//button[normalize-space(text())='EDIT']")
        self.edit_click = (By.XPATH , "//div[normalize-space(text())='07/17/2025']")

        #Actions

    def enter_username(self, username):
            self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def enter_sign_in (self):
        self.wait.until(EC.visibility_of_element_located(self.sign_field)).click()

    def entered_login(self):
        self.wait.until(EC.visibility_of_element_located(self.re_login)).click()

    def account_clicked(self):
        self.wait.until(EC.visibility_of_element_located(self.account_click)).click()

    def switch_to_new_window(self):
        # Switch Selenium focus to the newly opened window
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def account_transaction_click(self):
        transaction_menu = self.wait.until(EC.element_to_be_clickable(self.account_Transaction))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", transaction_menu)
        transaction_menu.click()
        print("✅ Clicked on 'Transactions' menu.")
        self.wait.until(EC.visibility_of_element_located(self.account_Transaction)).click()

    def opening_entry_click(self):
        # --- Hover over Opening Entries ---
        try:
            opening_entries = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Opening Entries"))
            )
        except:
            try:
                opening_entries = self.wait.until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Opening Entries"))
                )
            except:
                opening_entries = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Opening Entries']"))
                )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", opening_entries)
        self.actions.move_to_element(opening_entries).pause(0.5).perform()
        print("✅ Hovered over 'Opening Entries'")
        time.sleep(3)

        # --- Step 3: Click Ledger Account ---
        ledger_click_me = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ledger Opening B/L")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ledger_click_me)
        self.driver.execute_script("arguments[0].click();", ledger_click_me)
        print("✅ Clicked on 'Ledger account'")
        time.sleep(3)

    def Ledger_enter(self):
        ledger_field = self.wait.until(EC.element_to_be_clickable(self.ledger))
        ledger_field.send_keys(Keys.ENTER)
        print("✅ ENTER pressed on Ledger account")
        vat_account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='VAT RECEIVABLES A/C']"))
        )
        self.actions.move_to_element(vat_account).double_click(vat_account).perform()

    def add_amount_dr(self , amount):
        self.wait.until(EC.element_to_be_clickable(self.dr_amount)).send_keys(amount)

    def save_click(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
        print("Clicked on 'Save' button")

    def close_me(self):
        self.wait.until(EC.element_to_be_clickable(self.close_button)).click()
        print("Enter close button ")

    def edit_me(self):
        self.wait.until(EC.element_to_be_clickable(self.edits)).click()
        print("Click edit Button")

    def edit_section_double_click(self):
        element = self.wait.until(EC.element_to_be_clickable(self.edit_click))
        self.actions.double_click(element).perform()



        


