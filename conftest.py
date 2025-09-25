import pytest
from selenium import webdriver
@pytest.fixture
def driver():
   print('Open hours')
   driver = webdriver.Chrome()
   yield driver
   print('See you nex time')
   driver.quit()
