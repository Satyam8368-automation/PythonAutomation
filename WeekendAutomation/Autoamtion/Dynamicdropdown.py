import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(4)
checkbox=driver.find_elements(By.XPATH,"//div[@class='col-xs-12 remove-padding']//span//input")
time.sleep(4)
print(len(checkbox))
for checkbox1 in checkbox:
    checkbox1.click()
# driver.find_element(By.XPATH,"//input[@aria-controls='pr_id_1_list']").send_keys("r")
# time.sleep(5)
# station=driver.find_elements(By.XPATH,"//ul[@id='pr_id_1_list']//li")
# time.sleep(5)
# print(len(station))
# for station1 in station:
#     if station1.text.__contains__("RANCHI - RNC"):
#         station1.click()
#         break
