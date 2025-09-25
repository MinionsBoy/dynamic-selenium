import pytest
from utils.selenium_helpers import open_homepage, subscribe_newsletter

def test_verify_subscription_home(driver):
    open_homepage(driver)
    subscribe_newsletter(driver, "subhome@example.com")
    assert "You have been successfully subscribed!" in driver.page_source

def test_verify_subscription_cart(driver):
    open_homepage(driver)
    subscribe_newsletter(driver, "subcart@example.com", on_cart_page=True)
    assert "You have been successfully subscribed!" in driver.page_source
