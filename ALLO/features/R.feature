Feature:Test functionality


 Scenario: User enter the valid credentials for testing the login functionality.
   Given User open the login page.
   When User enter the data for username and password
   When User click on the Login button
   Then User should move to the next page


#   Examples:
#     | username | password |
#     | test     |test      |
