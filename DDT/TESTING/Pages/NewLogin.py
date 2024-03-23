# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from TESTING.Utilities.ReadProperties import properties
#
# if properties.get("Browser","browser")=="Chrome":
#  options = webdriver.ChromeOptions()
#  options.add_experimental_option("detach", True)
#  driver = webdriver.Chrome(options=options)
#  driver.get(properties.get("Login", "Url"))
#  driver.find_element(By.ID, properties.get("Locators", "username")).send_keys(properties.get("Login", "username"))
#  driver.find_element(By.ID, properties.get("Locators", "password")).send_keys(properties.get("Login", "password"))
#  driver.find_element(By.XPATH,properties.get("Locators","button")).click()
#
# if properties.get("Browser","browser2")=="Edge":
#  options = webdriver.EdgeOptions()
#  options.add_experimental_option("detach", True)
#  driver = webdriver.Edge(options=options)
#  driver.get(properties.get("Login", "Url"))
#  driver.find_element(By.ID, properties.get("Locators", "username")).send_keys(properties.get("Login", "username"))
#  driver.find_element(By.ID, properties.get("Locators", "password")).send_keys(properties.get("Login", "password"))
#  driver.find_element(By.XPATH,properties.get("Locators","button")).click()
#
#  if properties.get("Browser","browser1")=="Firefox":
#   options = webdriver.FirefoxOptions()
#   # options.add_experimental_option("detach", True)
#   driver = webdriver.Firefox(options=options)
#   driver.get(properties.get("Login", "Url"))
#   driver.find_element(By.ID, properties.get("Locators", "username")).send_keys(properties.get("Login", "username"))
#   driver.find_element(By.ID, properties.get("Locators", "password")).send_keys(properties.get("Login", "password"))
#   driver.find_element(By.XPATH,properties.get("Locators","button")).click()
