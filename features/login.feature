Feature: Login page
  In order to be able to login
  As a user
  I want to login only via valid credentials

  Background:
    Given User navigates to login form

  Scenario: As a user I want to login with valid credentials
    Given User submits "victoria@gmail.com" and "Testtest1234"
    Then User is logged into his account

  Scenario Outline: As a user I am not able to login with invalid credentials
    Given User submits "<username>" and "<password>"
    Then User sees login notification error
    Examples:
      | username                       | password                       |
      | test_username                  | test_password                  |
      | !@#$%^&*()_special_signs_check | !@#$%^&*()_special_signs_check |

  Scenario Outline: As a user I see form errors when I don't provide required credentials
    Given User submits "<username>" and "<password>"
    Then User sees login form error
    Examples:
      | username      | password      |
      | test_username |               |
      |               | test_password |
      |               |               |
