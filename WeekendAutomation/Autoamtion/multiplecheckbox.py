import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.thewebtaylor.com/static/tutorials/dummy-checkbox/")
checkbox=driver.find_elements(By.XPATH,"//ul[@class='dummy-checkbox multiple']//li")
for checkbox1 in checkbox:
    checkbox1.click()
time.sleep(4)
