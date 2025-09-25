

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_homepage(driver):
	driver.get("https://automationexercise.com/")
	assert "Automation Exercise" in driver.title

def login(driver, email, password):
	driver.find_element(By.LINK_TEXT, "Signup / Login").click()
	time.sleep(1)
	driver.find_element(By.NAME, "email").send_keys(email)
	driver.find_element(By.NAME, "password").send_keys(password)
	driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

def search_product(driver, product_name):
	search_box = driver.find_element(By.ID, "search_product")
	search_box.clear()
	search_box.send_keys(product_name)
	driver.find_element(By.ID, "submit_search").click()

def is_product_present(driver, product_name):
	products = driver.find_elements(By.XPATH, f"//h2[contains(text(), '{product_name}')]")
	return len(products) > 0

