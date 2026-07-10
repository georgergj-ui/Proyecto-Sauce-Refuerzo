import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

def test_cartpage_continueshoping_works(login_page, inventory_page, cart_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    buttons = inventory_page.add_cart_buttons()
    buttons[0].click()
    icon = inventory_page.cart_icon_validate()
    icon.click()
    assert cart_page.continue_shoping().is_displayed()
    button = cart_page.continue_shoping()
    button.click()
    assert "inventory.html" in cart_page.driver.current_url