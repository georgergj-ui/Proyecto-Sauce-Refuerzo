import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


def test_inventory_cart_icon_loaded(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.cart_icon_validate().is_displayed()


def test_inventory_hamburguer_nav_loaded(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.hamburguer_icon_validate().is_displayed()

def test_inventory_hamburger_sub_menu_loaded(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.hamburguer_icon_validate().click()
    options = inventory_page.hamburger_sub_menu_validate()

    expected_options = [
        "All Items",
        "About",
        "Logout",
        "Reset App State"
    ] 
    
    actual_options = []

    for option in options:
       actual_options.append(option.get_attribute("textContent"))

    assert actual_options == expected_options, "La lista no es la correcta, talvez un texto no es el esperado"


def test_inventory_has_six_products(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    products: list[WebElement] = inventory_page.inventory_products()
    assert len(products) == 6
    for product in products:
        assert product.is_displayed()


def test_inventory_sort_H_to_L(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_filter("Price (high to low)")
    first_product = inventory_page.product_names()[0]
    assert first_product.text == "Sauce Labs Fleece Jacket"

def test_inventory_sort_L_to_H(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_filter("Price (low to high)")
    first_product = inventory_page.product_names()[0]
    assert first_product.text == "Sauce Labs Onesie"

def test_inventory_sort_A_to_Z(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_filter("Name (A to Z)")
    first_product = inventory_page.product_names()[0]
    assert first_product.text == "Sauce Labs Backpack"

def test_inventory_sort_Z_to_A(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_filter("Name (Z to A)")
    first_product = inventory_page.product_names()[0]
    assert first_product.text == "Test.allTheThings() T-Shirt (Red)"

def test_inventory_add_product_update_cart_badge(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    buttons = inventory_page.add_cart_buttons()
    buttons[0].click()
    buttons[1].click()
    badge = inventory_page.cart_badge()
    assert badge.is_displayed()
    assert badge.text == "2", "Se estan agregando un numero incorrecto de Productos al carrito"
@pytest.mark.inventory
def test_inventory_add_product_and_remove_from_inventory(login_page, inventory_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    buttons = inventory_page.add_cart_buttons()
    buttons[0].click()
    buttons_remove = inventory_page.remove_cart_buttons()
    buttons_remove[0].click()
    badge = inventory_page.cart_badges()
    assert len(badge) == 0