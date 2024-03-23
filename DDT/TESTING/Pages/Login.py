from selenium.webdriver.common.by import By


class LoginPage():
    textbox_username_id ="user_login"
    textbox_password_id = "user_pass"
    button_login_xpath = "//input[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        # self.driver.findElement(self.textbox_username_id).clear()
        self.driver.findElement(By.ID,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        # self.driver.findElement(self.textbox_password_id).clear()
        self.driver.findElement(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
         self.driver.findElement(self.button_login_xpath).click()
