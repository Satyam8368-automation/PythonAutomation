from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_argument("--headless")
# options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.irctc.co.in/nget/train-search")
date=driver.find_element(By.XPATH,"(//input[@type='text'])[3]")
# driver.find_element(By.XPATH,"//a[text()='28']")
driver.execute_script("arguments[0].style.border='3px solid red'",date)
driver.save_screenshot('C:\\Users\\ADMIN\\PycharmProjects\\WeekendAutomation\\Screenshot\\2a.png')

