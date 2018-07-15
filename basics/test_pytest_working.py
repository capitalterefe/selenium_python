from selenium import webdriver
import os
class Test_RunnerClass():
    def test_withChrome(self):
        chromedriver='/Users/ct/Documents/devTools/chromedriver'
        os.environ['webdriver.chrome.driver']=chromedriver
        driver=webdriver.Chrome(chromedriver)
        driver.get('http://www.google.com')
        driver.close
        driver.quit
        print('test completed')
chromeTest=Test_RunnerClass()
chromeTest.test_withChrome()