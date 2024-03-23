import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,"//a[text()='Alert with Textbox ' ]").click()
driver.find_element(By.XPATH,"//button[text()='click the button to demonstrate the prompt box ']").click()
alert=Alert(driver)
print(alert.text)
time.sleep(4)
alert.send_keys("test")
time.sleep(4)
# alert.accept()
alert.dismiss()
