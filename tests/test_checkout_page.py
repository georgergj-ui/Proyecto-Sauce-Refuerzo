import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


@pytest.mark.check
def test_checkoutpage_inputs(login_page, inventory_page, cart_page, checkout_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_cart_buttons()[0].click()
    inventory_page.cart_icon_validate().click()
    
    cart_page.checkout_button().click()
    time.sleep(4)
    checkout_page.checkout_type_data("RUPEL", "TESTER", "66050")

    assert checkout_page.firstname_input().get_attribute("value") == "RUPEL"
    assert checkout_page.lastname_input().get_attribute("value") == "TESTER"
    assert checkout_page.zip_input().get_attribute("value") == "66050"
    
    checkout_page.continue_button().click()
    time.sleep(4)
    assert "checkout-step-two.html" in checkout_page.driver.current_url

    checkout_page.finish_button().click()
    assert "checkout-complete.html" in checkout_page.driver.current_url
    checkout_page.pdf().click()
    time.sleep(4)



def test_checkoutpage_validate_empty_fields(login_page, inventory_page, cart_page, checkout_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_cart_buttons()[0].click()
    inventory_page.cart_icon_validate().click()

    cart_page.checkout_button().click()

    checkout_page.continue_button().click()
    checkout_page.checkout_type_data("", "", "")
    
    error = checkout_page.error_message()
    assert error.is_displayed()
    assert "First Name is required" in error.text

@pytest.mark.check
def test_checkoutpage_goback(login_page, inventory_page, cart_page, checkout_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_cart_buttons()[0].click()
    inventory_page.cart_icon_validate().click()
    
    cart_page.checkout_button().click()
    time.sleep(4)
    checkout_page.checkout_type_data("RUPEL", "TESTER", "66050")

    assert checkout_page.firstname_input().get_attribute("value") == "RUPEL"
    assert checkout_page.lastname_input().get_attribute("value") == "TESTER"
    assert checkout_page.zip_input().get_attribute("value") == "66050"
    
    checkout_page.continue_button().click()
    time.sleep(4)
    assert "checkout-step-two.html" in checkout_page.driver.current_url

    checkout_page.finish_button().click()
    assert "checkout-complete.html" in checkout_page.driver.current_url
    checkout_page.back().click()
    
    assert "inventory.html" in checkout_page.driver.current_url
    time.sleep(4)