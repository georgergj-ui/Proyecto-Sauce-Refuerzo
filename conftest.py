import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import Loginpage
from pages.inventory_page import Inventorypage
from pages.cart_page import Cartpage
from pages.checkout_page import Checkoutpage

@pytest.fixture
def browser(scope="session"):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture
def login_page(browser):
    return Loginpage(browser)

@pytest.fixture
def inventory_page(browser):
    return Inventorypage(browser)

@pytest.fixture
def cart_page(browser):
    return Cartpage(browser)

@pytest.fixture
def checkout_page(browser):
    return Checkoutpage(browser)
