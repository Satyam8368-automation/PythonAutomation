import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
# driver.("https://blazedemo.com/login")
# driver.implicitly_wait(10)
driver.find_element(By.ID,"email").send_keys("TEST")
try:
   WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"password1"))
finally:
   driver.find_element(By.NAME,"password").send_keys("TESTST")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(2)
driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()
time.sleep(2)
driver.back()

# driver.find_element(By.PARTIAL_LINK_TEXT,"Password?").click()
time.sleep(2)
print(driver.title)
driver.forward()
driver.find_element(By.ID,"email").send_keys("TEST")
time.sleep(2)
driver.refresh()
time.sleep(2)
print(driver.current_url)
#
# driver=webdriver.Firefox()
# driver.get("https://blazedemo.com/login")
# print(driver.title)
# print(driver.current_url)
#
# driver=webdriver.Edge()
# driver.get("https://blazedemo.com/login")
# print(driver.title)
# print(driver.current_url)
