from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
import unittest
from pages.home.login_page import LoginPage


# class LogingTests(unittest.TestCase):
#     def test_validLogin(self):
#         print(sys.path)
#         print("webdriver module location"+webdriver.__file__)
#         chromedriver = "/Users/ct/Documents/devTools/chromedriver"
#         os.environ["webdriver.chrome.driver"] = chromedriver
#         driver = webdriver.Chrome(chromedriver)
#         baseUrl = "https://letskodeit.teachable.com/"
#         driver.maximize_window()
#         driver.implicitly_wait(3)
#         driver.get(baseUrl)
#         lp = LoginPage(driver)
#         lp.login("test@email.com", "abcabc")

#         userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']")
#         if userIcon is not None:
#             print("login successful")
#         else:
#             print('login failed')
from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        print(result)
        # self.assertTrue(result)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        print(result)
        # self.asserTrue(result)
