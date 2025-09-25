import pytest
from utils.selenium_helpers import open_homepage, signup, login, logout

def test_register_user(driver):
    open_homepage(driver)
    import uuid
    email = f"testcase1_{uuid.uuid4().hex[:8]}@example.com"
    signup(driver, "Test User", email, "TestPassword123!")
    assert "ACCOUNT CREATED!" in driver.page_source

def test_login_user_correct(driver):
    open_homepage(driver)
    login(driver, "validuser@example.com", "TestPassword123!")
    assert "Logged in as" in driver.page_source

def test_login_user_incorrect(driver):
    open_homepage(driver)
    login(driver, "wronguser@example.com", "wrongpass")
    assert "Your email or password is incorrect!" in driver.page_source

def test_logout_user(driver):
    open_homepage(driver)
    login(driver, "validuser@example.com", "TestPassword123!")
    logout(driver)
    assert "Login to your account" in driver.page_source

def test_register_existing_email(driver):
    open_homepage(driver)
    signup(driver, "Test User", "validuser@example.com", "TestPassword123!")
    assert "Email Address already exist!" in driver.page_source
