from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")
driver.maximize_window()
action=ActionChains(driver)
# rh=driver.find_element(By.XPATH,"//div[contains(text(),'Context / Right click for Menu')]")
hold=driver.find_element(By.XPATH,"//li[text()='C']")
action.click_and_hold(hold).perform()
# action.context_click(on_element=rh).perform()
# driver.get("https://jqueryui.com/droppable/")
# driver.maximize_window()
# frame=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# driver.switch_to.frame(frame)
# drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
# drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
# action=ActionChains(driver)
# action.drag_and_drop(drag,drop).perform()
