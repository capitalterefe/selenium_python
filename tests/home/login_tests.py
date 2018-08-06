from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
class LogingTests():
    def test_validLogin(self):
        baseUrl="https://letskodeit.teachable.com/"
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        lp=LoginPage(driver)
        lp.login("test@email.com","abcabc")
        
        
        userIcon=driver.find_element(By.XPATH,".//*[@id='navbar']")
        if userIcon is not None:
            print("login successful")
        else:
            print('login failed')



