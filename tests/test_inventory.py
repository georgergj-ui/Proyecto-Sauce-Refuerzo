import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.inventory
def test_inventory_cart_icon_loaded(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce" )
    assert inventory_page.cart_icon_validate().is_displayed()