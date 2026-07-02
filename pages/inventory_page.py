from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class Inventorypage (BasePage):
    CART = (By.ID, "shopping_cart_container")
    HAM = (By.ID, "react-burger-menu-btn")
    SUBMENU = (By.XPATH, "//nav[@class='bm-item-list']//a")
    PRODUCTS = (By.XPATH, "//div[@class='inventory_item']")
    FILTER =(By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_CART = (By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
    REMOVE_CART =(By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.btn_inventory")
    CART_BADGE =(By.CLASS_NAME, "shopping_cart_badge")

    def cart_icon_validate(self):
        return self.wait_for_element(self.CART)
    
    def hamburguer_icon_validate(self):
        return self.wait_for_element(self.HAM)
    
    def hamburger_sub_menu_validate(self):
        return self.driver.find_elements(*self.SUBMENU)
    
    def inventory_products(self):
        return self.driver.find_elements(*self.PRODUCTS)
    
    def sort_filter(self, option):
       dropdown = self.wait_for_element(self.FILTER)
       Select(dropdown).select_by_visible_text(option)

    def product_names(self):
        return self.driver.find_elements(*self.PRODUCT_NAMES)
    
    def add_cart_buttons(self):
        return self.driver.find_elements(*self.ADD_CART)
    
    def remove_cart_buttons(self):
        return self.driver.find_elements(*self.REMOVE_CART)
    
    def cart_badge(self):
       return self.wait_for_element(self.CART_BADGE)
    
    def cart_badges(self):
        return self.driver.find_elements(*self.CART_BADGE)
