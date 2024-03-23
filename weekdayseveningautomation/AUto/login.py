import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("TEST")
driver.find_element(By.NAME,"password").send_keys("RYARAC")
driver.find_element(By.NAME,"remember").click()
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
# driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Password?").click()
driver.back()
time.sleep(4)
driver.forward()
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("JAI HO")
driver.refresh()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("JAI HO")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(4)
print(driver.title)
driver.close()

