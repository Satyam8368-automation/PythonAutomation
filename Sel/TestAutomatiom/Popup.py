import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.automationtesting.in/Alerts.html")
# driver.find_element(By.XPATH,"//a[text()='Alert with OK & Cancel ']").click()
text=driver.find_element(By.XPATH,"//a[text()='Alert with Textbox ']")
driver.execute_script("arguments[0].click();",text)
driver.find_element(By.XPATH,"//button[text()='click the button to demonstrate the prompt box ']").click()
# driver.find_element(By.XPATH,"//button[@onclick='confirmbox()']").click()
# driver.find_element(By.XPATH,"//button[@onclick='alertbox()']").click()
alert=Alert(driver)
print(alert.text)
time.sleep(10)
alert.send_keys("TEST")
time.sleep(2)
alert.dismiss()
# alert.accept()
