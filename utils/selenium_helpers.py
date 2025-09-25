

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_homepage(driver):
	driver.get("https://automationexercise.com/")
	assert "Automation Exercise" in driver.title

def login(driver, email, password, timeout=10):
	driver.find_element(By.LINK_TEXT, "Signup / Login").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.NAME, "email"))
	)
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


def signup(driver, name, email, password, timeout=10):
	driver.find_element(By.LINK_TEXT, "Signup / Login").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.NAME, "name"))
	)
	driver.find_element(By.NAME, "name").send_keys(name)
	driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
	driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()
	# Wait for password field if it appears
	try:
		WebDriverWait(driver, 3).until(
			EC.visibility_of_element_located((By.ID, "password"))
		)
		driver.find_element(By.ID, "password").send_keys(password)
		driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
	except Exception:
		pass

def logout(driver):
	driver.find_element(By.LINK_TEXT, "Logout").click()

def get_cart_count(driver):
	cart_elem = driver.find_element(By.XPATH, "//a[@href='/view_cart']/span")
	return int(cart_elem.text) if cart_elem.text.isdigit() else 0


# Additional helpers for full test case coverage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os

def fill_contact_form(driver, name, email, subject, message, file_path=None, timeout=10):
	driver.find_element(By.LINK_TEXT, "Contact us").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.NAME, "name"))
	)
	driver.find_element(By.NAME, "name").send_keys(name)
	driver.find_element(By.NAME, "email").send_keys(email)
	driver.find_element(By.NAME, "subject").send_keys(subject)
	driver.find_element(By.ID, "message").send_keys(message)
	if file_path and os.path.exists(file_path):
		driver.find_element(By.NAME, "upload_file").send_keys(file_path)
	driver.find_element(By.NAME, "submit").click()
	try:
		Alert(driver).accept()
	except Exception:
		pass

def go_to_test_cases_page(driver, timeout=10):
	driver.find_element(By.LINK_TEXT, "Test Cases").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Test Cases')]") )
	)

def view_all_products(driver, timeout=10):
	driver.find_element(By.LINK_TEXT, "Products").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]") )
	)

def view_product_detail(driver, product_index=0, timeout=10):
	view_all_products(driver)
	products = driver.find_elements(By.XPATH, "//a[contains(text(),'View Product')]")
	if products and len(products) > product_index:
		products[product_index].click()
		WebDriverWait(driver, timeout).until(
			EC.visibility_of_element_located((By.XPATH, "//div[@class='product-information']"))
		)

def add_product_to_cart(driver, product_index=0, timeout=10):
	view_all_products(driver)
	add_btns = driver.find_elements(By.XPATH, "//a[contains(text(),'Add to cart')]")
	if add_btns and len(add_btns) > product_index:
		add_btns[product_index].click()
		WebDriverWait(driver, timeout).until(
			EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Continue Shopping')]"))
		)
		driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]" ).click()

def go_to_cart(driver, timeout=10):
	driver.find_element(By.LINK_TEXT, "Cart").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Shopping Cart')]") )
	)

def remove_product_from_cart(driver, timeout=10):
	go_to_cart(driver)
	delete_btns = driver.find_elements(By.CLASS_NAME, "cart_quantity_delete")
	if delete_btns:
		delete_btns[0].click()
		WebDriverWait(driver, timeout).until(
			EC.invisibility_of_element_located((By.CLASS_NAME, "cart_quantity_delete"))
		)

def subscribe_newsletter(driver, email, on_cart_page=False, timeout=10):
	if on_cart_page:
		go_to_cart(driver)
	email_box = driver.find_element(By.ID, "susbscribe_email")
	email_box.clear()
	email_box.send_keys(email)
	driver.find_element(By.ID, "subscribe").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'You have been successfully subscribed!')]") )
	)

def place_order(driver, name, card_number, cvc, expiry, timeout=10):
	go_to_cart(driver)
	driver.find_element(By.XPATH, "//a[contains(text(),'Proceed To Checkout')]").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Address Details')]") )
	)
	driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys("Test order")
	driver.find_element(By.XPATH, "//a[contains(text(),'Place Order')]").click()
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.NAME, "name_on_card"))
	)
	driver.find_element(By.NAME, "name_on_card").send_keys(name)
	driver.find_element(By.NAME, "card_number").send_keys(card_number)
	driver.find_element(By.NAME, "cvc").send_keys(cvc)
	driver.find_element(By.NAME, "expiry_month").send_keys(expiry[:2])
	driver.find_element(By.NAME, "expiry_year").send_keys(expiry[2:])
	driver.find_element(By.ID, "submit").click()

def download_invoice(driver, timeout=10):
	WebDriverWait(driver, timeout).until(
		EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Download Invoice')]"))
	)
	driver.find_element(By.XPATH, "//a[contains(text(),'Download Invoice')]").click()

def scroll_up(driver):
	driver.execute_script("window.scrollTo(0, 0);")

def scroll_down(driver):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def add_review(driver, name, email, review, product_index=0, timeout=10):
	view_product_detail(driver, product_index)
	driver.find_element(By.ID, "name").send_keys(name)
	driver.find_element(By.ID, "email").send_keys(email)
	driver.find_element(By.ID, "review").send_keys(review)
	driver.find_element(By.ID, "button-review").click()

