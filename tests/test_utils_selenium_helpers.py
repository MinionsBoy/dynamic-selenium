import pytest
from utils import selenium_helpers

# These tests assume a working Selenium driver fixture named 'driver' is available (from conftest.py)

def test_open_homepage(driver):
    selenium_helpers.open_homepage(driver)
    assert "Automation Exercise" in driver.title

def test_login_logout(driver):
    selenium_helpers.open_homepage(driver)
    # Use a valid user for this test
    selenium_helpers.login(driver, "validuser@example.com", "TestPassword123!")
    assert "Logged in as" in driver.page_source
    selenium_helpers.logout(driver)
    assert "Login to your account" in driver.page_source

def test_signup_existing_email(driver):
    selenium_helpers.open_homepage(driver)
    selenium_helpers.signup(driver, "Test User", "validuser@example.com", "TestPassword123!")
    assert "Email Address already exist!" in driver.page_source

def test_search_and_product_present(driver):
    selenium_helpers.open_homepage(driver)
    selenium_helpers.search_product(driver, "Tshirt")
    assert selenium_helpers.is_product_present(driver, "Tshirt") or "SEARCHED PRODUCTS" in driver.page_source

def test_cart_count(driver):
    selenium_helpers.open_homepage(driver)
    selenium_helpers.add_product_to_cart(driver)
    count = selenium_helpers.get_cart_count(driver)
    assert count >= 1
