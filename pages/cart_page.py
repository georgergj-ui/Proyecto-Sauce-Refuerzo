import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class Cartpage (BasePage):
    CONTINUESHOPING = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_medium")




    def continue_shoping(self):
        return self.wait_for_element(self.CONTINUESHOPING)
    