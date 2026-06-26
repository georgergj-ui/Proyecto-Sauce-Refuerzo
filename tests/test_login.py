import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_saucedemo(login_page):
    login_page.navigate_login() #ESTO ES UN WEB ELEMENT---

def test_login_page_elements_are_displayed(login_page):
    login_page.navigate_login()

    assert login_page.login_button().is_displayed()
    assert login_page.username_input().is_displayed()
    assert login_page.password_input().is_displayed()


def test_valid_login(login_page):
    login_page.navigate_login()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in login_page.driver.current_url
    time.sleep(4)

@pytest.mark.negative
def test_empty_username(login_page):
    login_page.navigate_login()
    login_page.login("", "secret_sauce")
    error = login_page.error_message()
    assert error.is_displayed()
    assert "Username is required" in error.text

@pytest.mark.negative
def test_empty_password(login_page):
    login_page.navigate_login()
    login_page.login("standard_user", "")
    error = login_page.error_message()
    assert error.is_displayed()
    assert "Epic sadface" in error.text

@pytest.mark.negative
def test_invalid_login(login_page):
    login_page.navigate_login()
    login_page.login("invalid_user", "invalid_password")
    error = login_page.error_message()
    assert error.is_displayed()


@pytest.mark.negative
def test_locked_out_user(login_page):
    login_page.navigate_login()
    login_page.login("locked_out_user","secret_sauce")
    error = login_page.error_message()
    assert error.is_displayed()
    assert "locked out" in error.text



   