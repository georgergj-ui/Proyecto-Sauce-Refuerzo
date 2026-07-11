import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class Cartpage (BasePage):
    CONTINUESHOPING = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_medium")
    REMOVEBTN = (By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.cart_button")
    REMOVEDITEM = (By.XPATH, "//div[@class='removed_cart_item']")
    CART_ITEMS = (By.XPATH, "//div[@data-test='inventory-item']")
    CHECKOUT = (By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    CART_BADGES =(By.CLASS_NAME, "shopping_cart_badge")

    def continue_shoping(self):
        return self.wait_for_element(self.CONTINUESHOPING)
    def remove_button(self):
        return self.wait_for_element(self.REMOVEBTN)
    def removed_item(self):
        return self.wait_for_element(self.REMOVEDITEM)
    def cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)
    def wait_until_cart_item_disappears(self):
        self.wait_until_disappears(self.CART_ITEMS)
    def checkout_button(self):
        return self.wait_for_element(self.CHECKOUT)
    def cart_badges(self):
        return self.wait_for_element(self.CART_BADGES)