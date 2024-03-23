import unittest

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def testName(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://blazedemo.com/login")
        title = driver.title
        # self.assertNotEquals(driver.title, "BlazeDemo")
        self.assertTrue((title == "BlazeDemo") & (title == "BlazeDemo"), "Matchinhg header")
        driver.find_element(By.ID, "email").send_keys("SATYAM")
