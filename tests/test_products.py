import pytest
from utils.selenium_helpers import open_homepage, search_product, is_product_present, view_all_products, view_product_detail, add_product_to_cart, go_to_cart, add_review
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_product(driver):
    open_homepage(driver)
    search_product(driver, "Tshirt")
    assert "SEARCHED PRODUCTS" in driver.page_source

def test_is_product_present(driver):
    open_homepage(driver)
    search_product(driver, "Tshirt")
    assert is_product_present(driver, "Tshirt")

def test_verify_all_products_and_detail(driver):
    open_homepage(driver)
    view_all_products(driver)
    assert "All Products" in driver.page_source
    view_product_detail(driver)
    assert "Category" in driver.page_source or "product-information" in driver.page_source

def test_add_review_on_product(driver):
    open_homepage(driver)
    add_review(driver, "Test User", "review@example.com", "Great product!")
    assert "Thank you for your review." in driver.page_source or "success" in driver.page_source.lower()

def test_view_category_products(driver):
    open_homepage(driver)
    driver.find_element(By.LINK_TEXT, "Women").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Women - Dress Products')]"))
    )
    assert "Women - Dress Products" in driver.page_source

def test_view_and_cart_brand_products(driver):
    open_homepage(driver)
    driver.find_element(By.LINK_TEXT, "Brands").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Brands')]"))
    )
    assert "Brands" in driver.page_source
