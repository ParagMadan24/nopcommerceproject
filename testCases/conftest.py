import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def setup(browser):
    service = Service()
    if browser=="Chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

