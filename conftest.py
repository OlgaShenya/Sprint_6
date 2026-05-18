import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from url import BASE_URL


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def main_page(driver):
    driver.get(BASE_URL)
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    driver.get(BASE_URL)
    page = OrderPage(driver)
    page.accept_cookies_if_present()
    return page
