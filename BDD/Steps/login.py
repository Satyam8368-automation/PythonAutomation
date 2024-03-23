from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class login:


  @given(u'Navigate to login page')
  def step_naviagte_page(context):
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    context.driver=webdriver.Chrome()
    context.driver.get("https://blazedemo.com/login")

  @when(u'Enter the value of username "{username}"')
  def step_enter_username(context,username):
    context.driver.find_element(By.ID,"email").send_keys(username)

  @when(u'Enter the value of password "{password}"')
  def step_enter_password(context,password):
        context.driver.find_element(By.ID,"password").send_keys(password)

  @when(u'Click on the login')
  def step_click_button(context):
       context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

  @then(u'Successfully login')
  def step_title(context):
         print(context.driver.title)
