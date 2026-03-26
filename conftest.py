import pytest
from selenium import webdriver
from data.urls import Urls

@pytest.fixture
def driver():
    
    driver = webdriver.Chrome()
    driver.get(Urls.main_url)
    driver.maximize_window()
    yield driver
    driver.quit()
