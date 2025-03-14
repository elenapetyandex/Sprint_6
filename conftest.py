import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()









