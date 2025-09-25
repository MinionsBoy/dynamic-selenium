import pytest
from utils.selenium_helpers import open_homepage, go_to_test_cases_page, scroll_up, scroll_down
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_test_cases_page(driver):
    open_homepage(driver)
    go_to_test_cases_page(driver)
    assert "Test Cases" in driver.page_source

def test_scroll_up_arrow_and_down(driver):
    open_homepage(driver)
    scroll_down(driver)
    driver.find_element(By.ID, "scrollUp").click()
    scroll_up(driver)
    assert driver.execute_script("return window.pageYOffset;") == 0

def test_scroll_up_without_arrow_and_down(driver):
    open_homepage(driver)
    scroll_down(driver)
    scroll_up(driver)
    assert driver.execute_script("return window.pageYOffset;") == 0
