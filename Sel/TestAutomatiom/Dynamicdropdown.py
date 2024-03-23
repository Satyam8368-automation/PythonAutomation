import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@aria-controls='pr_id_1_list']").send_keys("R")
time.sleep(10)
from1 = driver.find_elements(By.XPATH, "//ul[@id='pr_id_1_list']//li")
time.sleep(10)
print(len(from1))
for form2 in from1:
    if form2.text.__contains__("RANCHI - RNC"):
        form2.click()
        break
