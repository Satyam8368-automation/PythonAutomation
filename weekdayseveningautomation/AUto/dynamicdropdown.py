import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@aria-controls='pr_id_1_list']").send_keys("r")
time.sleep(6)
drop=driver.find_elements(By.XPATH,"//ul[@id='pr_id_1_list']//li")
print(len(drop))
for drops in drop:
    if(drops.text.__contains__("RANCHI - RNC")):
        drops.click()
        break

