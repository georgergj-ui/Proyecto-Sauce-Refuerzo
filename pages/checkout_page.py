import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class Checkoutpage(BasePage):
    FIRSTN_INPUT = (By.ID, "first-name")
    LASTN_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE = (By.XPATH, "//input[@data-test='continue']")
    GETERROR = (By.XPATH, "//h3[@data-test='error']")
    FINISH = (By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button")
    PDF =(By.ID, "generate-pdf-order")
    BACK =(By.ID, "back-to-products")

    def firstname_input(self):
        return self.wait_for_element(self.FIRSTN_INPUT)
    def lastname_input(self):
        return self.wait_for_element(self.LASTN_INPUT)
    def zip_input(self):
        return self.wait_for_element(self.ZIP_INPUT)
    
    def continue_button(self):
        return self.wait_for_element(self.CONTINUE)
    
    
    def checkout_type_data(self, firstname, lastname, zipcode):
        self.type_text(self.FIRSTN_INPUT,firstname)
        self.type_text(self.LASTN_INPUT, lastname)
        self.type_text(self.ZIP_INPUT, zipcode)

    def error_message(self):
        return self.wait_for_element(self.GETERROR)
    
    def finish_button(self):
        return self.wait_for_element(self.FINISH)
    def pdf(self):
        return self.wait_for_element(self.PDF)
    def back(self):
        return self.wait_for_element(self.BACK)
    
    