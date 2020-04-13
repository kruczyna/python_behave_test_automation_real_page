from behave import given, use_step_matcher, then
from behave.runner import Context

use_step_matcher("re")


@given('User navigates to login form')
def navigate_to_login_form(context: Context) -> None:
    context.login_page.navigate_to_login_form()


@given('User submits "([^"]*)" and "([^"]*)"')
def submit_login_credentials(context: Context, username: str, password: str) -> None:
    context.login_page.submit_login_credentials(username, password)


@then('User sees login form error')
def login_form_error(context: Context) -> None:
    context.login_page.login_form_error()


@then('User sees login notification error')
def login_notification_error(context: Context) -> None:
    context.login_page.login_notification_error()
