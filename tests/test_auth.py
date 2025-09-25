import pytest
from utils.selenium_helpers import open_homepage, signup, login, logout

def test_register_user(driver, random_email):
    open_homepage(driver)
    signup(driver, "Test User", random_email, "TestPassword123!")
    assert "ACCOUNT CREATED!" in driver.page_source

def test_login_user_correct(driver, test_user):
    open_homepage(driver)
    login(driver, test_user["email"], test_user["password"])
    assert "Logged in as" in driver.page_source

def test_login_user_incorrect(driver):
    open_homepage(driver)
    login(driver, "wronguser@example.com", "wrongpass")
    assert "Your email or password is incorrect!" in driver.page_source

def test_logout_user(driver, test_user):
    open_homepage(driver)
    login(driver, test_user["email"], test_user["password"])
    logout(driver)
    assert "Login to your account" in driver.page_source

def test_register_existing_email(driver, test_user):
    open_homepage(driver)
    signup(driver, test_user["name"], test_user["email"], test_user["password"])
    assert "Email Address already exist!" in driver.page_source
