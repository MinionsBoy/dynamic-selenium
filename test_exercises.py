

import pytest
from utils.selenium_helpers import open_homepage, search_product, is_product_present

def test_open_homepage(driver):
	open_homepage(driver)

def test_search_product(driver):
	open_homepage(driver)
	search_product(driver, "Tshirt")
	assert "SEARCHED PRODUCTS" in driver.page_source

def test_is_product_present(driver):
	open_homepage(driver)
	search_product(driver, "Tshirt")
	assert is_product_present(driver, "Tshirt")

