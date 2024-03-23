import time

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")


def capture_screenshot(d,path):
   file_name=path +"screenshot"+ time.asctime().replace(":","_")+".png"
   login=driver.find_element(By.XPATH,"//button[@type='submit']")
   driver.execute_script("arguments[0].style.border='3px solid red'",login)
   time.sleep(3)
   d.save_screenshot(file_name)

capture_screenshot(driver,"C:\\Users\\ADMIN\\PycharmProjects\\Sel\\TestAutomatiom")
