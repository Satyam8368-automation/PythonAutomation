from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("SATYAM")
action=ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# action.key_down(Keys.TAB).key_up(Keys.TAB)
action.send_keys(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
# action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
action.send_keys(Keys.ENTER).perform()
# action.send_keys(Keys.RETURN).perform()

