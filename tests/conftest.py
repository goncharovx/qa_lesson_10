import allure
import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
@allure.step("Настройка браузера")
def browser_set():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://github.com"
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture(scope="session", autouse=True)
@allure.step("Выключение браузера")
def browser_teardown():
    yield
    browser.quit()
