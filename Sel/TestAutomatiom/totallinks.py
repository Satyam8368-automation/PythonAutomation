from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
ls=driver.find_elements(By.TAG_NAME,"a")
print(len(ls))
for ls1  in ls:
    print(ls1.get_attribute("href"))
    print(ls1.text)

# /button:-->button, text field==> input, div:-->div,checkbox:--> input, frame:--> iframe
