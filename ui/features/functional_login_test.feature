Feature: As a user, I want to login with a username and password in order to access the application.

  Background:
    Given the dashboard page is open

  Scenario: Login with a valid username and password
    When I click the Sign In button in the header
    #Then I should see the login page
    When I enter the username in the field
    And I enter the password in the field
    And I press the Sign In button
    Then I should see the dashboard page
    And I log into my account
