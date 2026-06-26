from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class Inventorypage (BasePage):
    CART = (By.ID, "shopping_cart_container")

    def cart_icon_validate(self):
        return self.wait_for_element(self.CART)