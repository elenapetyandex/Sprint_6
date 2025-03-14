import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.SCOOTER_ORDER_URL)
    yield driver
    driver.quit()



@pytest.fixture
def driver_1(driver):
    driver.get(Urls.SCOOTER_HOMEPAGE_URL)
    yield driver
    driver.quit()




