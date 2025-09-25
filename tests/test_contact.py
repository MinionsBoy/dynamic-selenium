import pytest
from utils.selenium_helpers import open_homepage, fill_contact_form

def test_contact_us_form(driver, tmp_path):
    open_homepage(driver)
    file_path = str(tmp_path / "testfile.txt")
    with open(file_path, "w") as f:
        f.write("test file upload")
    fill_contact_form(driver, "Test User", "test@example.com", "Subject", "Message", file_path)
    assert "Success! Your details have been submitted successfully." in driver.page_source
