import pytest
import os
from selenium.webdriver import Chrome

@pytest.fixture
def webdriver(request):
    chromedriver='/Users/ct/Documents/devTools/chromedriver'
    os.environ['webdriver.chrome.driver']=chromedriver
    driver=Chrome(chromedriver)
    request.addfinalizer(driver.quit)
    return driver

def test_nix_website_title(webdriver):
    webdriver.get("https://nixos.org/nix")
    assert 'Nix' in webdriver.title
def test_yahoo_website_title(webdriver):
    webdriver.get("https://yahoo.com")
    print(webdriver.title)
    assert 'Yahoo' in webdriver.title
def test_pytest_website_title(webdriver):
    webdriver.get("https://pytest.org/latest")
    assert 'pytest' in webdriver.title