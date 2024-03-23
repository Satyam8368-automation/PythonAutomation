Feature: Login with the credentials

  Scenario Outline: Try to login with valid credentails
    Given Navigate to login page
    When Enter the value of username "<username>"
    When Enter the value of password "<password>"
    When Click on the login
    Then Successfully login

#    When enter the value of insured name "<>"
    Examples:
      | username | password |
      |Test      |Test@1    |
      |TEST@1    |Satay@21  |
