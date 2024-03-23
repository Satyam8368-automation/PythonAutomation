import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.automationtesting.in/Windows.html")
print("parent window:"+driver.title)
button=driver.find_element(By.XPATH,"//button[text()='    click   ']")
action=ActionChains(driver)
action.click(button).perform()
time.sleep(4)
driver.switch_to.window(driver.window_handles[1])
print("Child window:"+driver.title)
srl=driver.find_element(By.XPATH,"//h4[text()='Selenium 4.17 Released!']")
action.scroll_to_element(srl).perform()
time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print("parent window:"+driver.title)
