Feature: Registration page
  In order to be able to register an account
  As a user
  I want to fill out registration form

  Background:
    Given User logs into fitatu application

  Scenario: As a user I want to see which fields are required in update profile
    Given User submits an empty initial profile form
    Then User sees required fields errors

  Scenario: As a user I want to submit initial profile with minimum data necessary
    Given User submits "170" as height, "80" as current weight and "70" as goal weight
    Then User navigates to thank you page
    And User logs out of the application
