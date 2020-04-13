Feature: Registration page
  In order to be able to register an account
  As a user
  I want to fill out registration form

  Background:
    Given User navigates to registration form

  Scenario: As a user I want to see which fields are required
    When User submits an empty registration form
    Then User sees which fields are required

  Scenario Outline: As a user I want to have register form fields validated
    When User inputs invalidly formatted "<email>" and "<password>"
    Then User sees register form validation error
    Examples:
      | email               | password                                         |
      | test                | test                                             |
      | test@test           | 1                                                |
      | valid@email.address | short                                            |
      | test                | validPassword                                    |
      | valid@email.address | 123456789012345678901234567890_too_long_password |

  Scenario: As a user I want to register an account
    When User submits valid register credentials
    Then I navigate to profile settings
