Feature: Login funcationality

  Scenario:Validate login functionality with blank credentials
    Given User try to login
    When User don't enter value of username and password
    When user click on the login button
    Then User will not navigate to next page

   Scenario:Validate login functionality with  credentials
    Given User try to login
    When User enter value of username and password
    When user click on the login button
    Then User will not navigate to next page

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




