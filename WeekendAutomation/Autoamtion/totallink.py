import unittest

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def testcase(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.w3.org/Provider/Style/dummy.html")
        self.assertNotEquals(driver.title, "BlazDemo")
        links=driver.find_elements(By.TAG_NAME,"a")
        print(len(links))
# for link in links:
#     print(link.text)
#     print(link.get_attribute("href"))
