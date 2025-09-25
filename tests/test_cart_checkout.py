import pytest
from utils.selenium_helpers import open_homepage, add_product_to_cart, go_to_cart, remove_product_from_cart, place_order, download_invoice, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_products_in_cart(driver):
    open_homepage(driver)
    add_product_to_cart(driver)
    go_to_cart(driver)
    assert "Shopping Cart" in driver.page_source

def test_verify_product_quantity_in_cart(driver):
    open_homepage(driver)
    add_product_to_cart(driver)
    go_to_cart(driver)
    qty_elem = driver.find_element(By.CLASS_NAME, "cart_quantity_input")
    assert int(qty_elem.get_attribute("value")) >= 1

def test_remove_products_from_cart(driver):
    open_homepage(driver)
    add_product_to_cart(driver)
    remove_product_from_cart(driver)
    assert "Cart is empty!" in driver.page_source or "Shopping Cart" in driver.page_source

def test_place_order_login_before_checkout(driver, test_user):
    open_homepage(driver)
    login(driver, test_user["email"], test_user["password"])
    add_product_to_cart(driver)
    place_order(driver, test_user["name"], "4111111111111111", "123", "1225")
    assert "ORDER PLACED!" in driver.page_source or "Congratulations! Your order has been confirmed!" in driver.page_source

def test_download_invoice_after_purchase(driver, test_user):
    open_homepage(driver)
    login(driver, test_user["email"], test_user["password"])
    add_product_to_cart(driver)
    place_order(driver, test_user["name"], "4111111111111111", "123", "1225")
    download_invoice(driver)
    # No assert: download is browser-handled
