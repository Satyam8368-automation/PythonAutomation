from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
options.add_argument("--headless")
driver= webdriver.Chrome(options=options)
driver.get("https://demo.automationtesting.in/Windows.html")
print("parent window : " +driver.title)
driver.find_element(By.XPATH,"//button[text()='    click   ']").click()
driver.switch_to.window(driver.window_handles[1]) #child window
print("child window : " +driver.title)
driver.switch_to.window(driver.window_handles[0]) #parent window
print("again parent window : " +driver.title)
