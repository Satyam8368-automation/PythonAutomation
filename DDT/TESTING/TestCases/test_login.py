import pytest

from TESTING.TestCases.conftest import setup
from TESTING.Pages.Login import LoginPage
from TESTING.Utilities.ReadProperties import properties

pytest.mark.usefixtures("conftest")

# @pytest.mark.usefixtures("setup")
def test_login(setup):
    driver=setup
    driver.get(properties.get("Login", "URL"))
    loginpage=LoginPage(driver)
    loginpage.setusername("username")
    loginpage.setpassword("username")
    loginpage.clickLogin()
    loginpage_title = driver.title
    if loginpage_title == "wisemenseries":
        assert True
    else:
        driver.save_sreenshot(".\\Screenshot\\" + "test_loginpage.png")
        driver.close()
        assert False
