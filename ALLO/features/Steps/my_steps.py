
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# from Features.Utilities import ConfigReader
# from Features.pages.Loginpage import LoginPage
# from Features.Support.environment import before_scenario


# log=LoginPage

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
@given('User open the login page.')
def step_giv(context):
   driver.get("https://blazedemo.com/login")

@when('User enter the data for username and password')
def steps_when_enter_username_password(context):
   driver.find_element(By.ID,"email").send_keys("SATYAM")
   driver.find_element(By.ID,"password").send_keys("SATYAM")
   # context.log=LoginPage(context.driver)
   # context.log.enter(username)
   # context.log.passw(password)
   # # raise NotImplementedError(u'STEP: When User enter the data for test and test')




@when('User click on the Login button')
def step_login(context):
   driver.find_element(By.XPATH,"//button[@type='submit']").click()





@then('User should move to the next page')
def step_title(context):
   print(context.driver.title)

