import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


def getData():
    return [("harshitducat08", "Harshit9457490522@",
             "https://wisemenseries.in/wp-login.php?redirect_to=https%3A%2F%2Fwisemenseries.in%2Fwp-admin%2F&reauth=1")]


@pytest.mark.parametrize("username,password,url", getData())
def test_login(username, password, url):
    driver.get(url)
    driver.find_element(By.ID, "user_login").send_keys(username)
    driver.find_element(By.ID, "user_pass").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()


pytest.main(["--html=trt.html"])
