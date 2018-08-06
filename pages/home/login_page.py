from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    
    #locators
    _login_link="Login"
    _email_field="user_email"
    _password_field="user_password"
    _login_button="commit"


    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT,self._login_link)

    def login(self,userName,password):
       self.driver.find_element(By.LINK_TEXT,self._login_link).click()
       self.driver.find_element(By.ID,self._email_field).send_keys(userName)
       self.driver.find_element(By.ID,self._password_field).send_keys(password)
       self.driver.find_element(By.NAME,self._login_button).click()
        


        