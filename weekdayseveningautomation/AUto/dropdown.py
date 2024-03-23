import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
driver.maximize_window()
driver.find_element(By.XPATH,"//select[@id='first']//option[text()='Iphone']").click()
# select=Select(driver.find_element(By.XPATH,"//select[@id='first']"))
# select.select_by_index(3)
# time.sleep(5)
# select.select_by_value("Google")
# time.sleep(5)
# select.select_by_visible_text("Iphone")
# time.sleep(5)
