from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User try to login')
def step_naviagte_page(context):
     options=webdriver.ChromeOptions()
     options.add_experimental_option("detach",True)
     context.driver=webdriver.Chrome()
     context.driver.get("https://blazedemo.com/login")

@when(u'User don\'t enter value of username and password')
def step_impl(context):
    context.driver.find_element(By.ID,"email").send_keys("")
    context.driver.find_element(By.ID,"password").send_keys("")

@when(u'User enter value of username and password')
def step_impl(context):
    context.driver.find_element(By.ID,"email").send_keys("TEST")
    context.driver.find_element(By.ID,"password").send_keys("REST")

@when(u'user click on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()


@then(u'User will not navigate to next page')
def step_impl(context):
    print(context.driver.title)

