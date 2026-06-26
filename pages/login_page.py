from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class Loginpage(BasePage):
    LOGINBUTTON = (By.ID, "login-button") #LOCATORS-----------------
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    GETERROR = (By.XPATH, "//h3[@data-test='error']")

    def navigate_login(self): #METHODS-----------------------------
        self.navigate_to("https://www.saucedemo.com/")

    def login_button(self):
        return self.wait_for_element(self.LOGINBUTTON)
    def username_input(self):
        return self.wait_for_element(self.USERNAME_INPUT)
    def password_input(self):
        return self.wait_for_element(self.PASSWORD_INPUT)
    
    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGINBUTTON)

    def error_message(self):
        return self.wait_for_element(self.GETERROR)