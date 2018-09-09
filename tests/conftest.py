import pytest
from selenium import webdriver
import os
import sys
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on FF")
    # else:
    #     baseURL = "https://letskodeit.teachable.com/"
    #     chromedriver = "/Users/ct/Documents/devTools/chromedriver"
    #     os.environ["webdriver.chrome.driver"] = chromedriver
    #     driver = webdriver.Chrome(chromedriver)
    #     driver.get(baseURL)
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
