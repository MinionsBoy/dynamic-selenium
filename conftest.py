import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
   return "https://automationexercise.com/"

@pytest.fixture(scope="session")
def test_user():
   # Update as needed for your environment
   return {
      "email": "validuser@example.com",
      "password": "TestPassword123!",
      "name": "Test User"
   }


# Additional fixtures for test data
@pytest.fixture
def random_email():
   return f"autouser_{uuid.uuid4().hex[:8]}@example.com"

@pytest.fixture
def product_name():
   return "Tshirt"

@pytest.fixture
def review_text():
   return "Great product!"

@pytest.fixture(scope="session")
def driver():
   print('Open browser session')
   options = Options()
   options.add_argument('--start-maximized')
   # options.add_argument('--headless')  # Uncomment for headless mode
   driver = webdriver.Chrome(options=options)
   yield driver
   print('Closing browser session')
   driver.quit()
