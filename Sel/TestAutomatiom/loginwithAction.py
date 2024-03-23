from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
username=driver.find_element(By.ID,"email")
driver.execute_script("arguments[0].value='satyam';",username)
actions=ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
actions.send_keys(Keys.TAB).perform()
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
psw=driver.find_element(By.ID,"password")
actions.send_keys(Keys.TAB).perform()
check=driver.find_element(By.XPATH,"//input[@type='checkbox']")
actions.click(on_element=check)
actions.send_keys(Keys.TAB).perform()
login=driver.find_element(By.XPATH,"//button[@type='submit']")
actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.save_screenshot("Test.png")
