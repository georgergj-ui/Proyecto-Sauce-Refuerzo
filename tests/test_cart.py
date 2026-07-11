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


def test_cart_remove_item(login_page, inventory_page, cart_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_cart_buttons()[0].click()
    inventory_page.cart_icon_validate().click()
    
    cart_page.remove_button().click()
    cart_page.wait_until_cart_item_disappears()

    assert len(cart_page.cart_items()) == 0




def test_cart_checkout_button(login_page, inventory_page, cart_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_cart_buttons()[0].click()
    inventory_page.cart_icon_validate().click()

    cart_page.checkout_button().click()

    assert "checkout-step-one.html" in cart_page.driver.current_url

@pytest.mark.cart
def test_cart_checkout_icon_equals_item(login_page, inventory_page, cart_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")

    items = inventory_page.add_cart_buttons()
    items[0].click()
    items[1].click()
    items[2].click()
    items[3].click()
    items[4].click()
    items[5].click()
    inventory_page.cart_icon_validate().click()


    assert len(cart_page.cart_items()) == 6
    badge = cart_page.cart_badges()
    assert badge.text == "6" , "Se estan agregando numero incorrecto al carrito"
