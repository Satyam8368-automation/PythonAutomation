import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def getData():
    return [("test@12.com", "test@12", "https://www.orangehrm.com/en/book-a-free-demo/")]


@pytest.mark.parametrize("username,password,url", getData())
def test_login(username, password, url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # driver.find_element(By.XPATH,"//input[@id='Form_getForm_subdomain']").send_keys(username)
    # driver.find_element(By.XPATH,"//input[@id='Form_getForm_Name']").send_keys(password)
    print(username)
    print(password)

pytest.main(["--html=trt.html"])
#
# def test_name():
#     print("dfwe")
#
# def test_res():
#     print("dew")
#
# def test_cal():
#     assert 1+2==3
