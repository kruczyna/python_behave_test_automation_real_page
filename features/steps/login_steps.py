from behave import given, use_step_matcher, then, step
from behave.runner import Context

from features.helpers.decorators import delete_all_cookies

use_step_matcher("re")


@given('User navigates to login form')
def navigate_to_login_form(context: Context) -> None:
    context.login_page.navigate_to_login_form()


# Used step matcher to match empty values.
# If you don't want to have empty values in a scenario outline,
# you can map regular variables within step name.
# In this case "{username}" and "{password}"
@delete_all_cookies
@given('User submits "([^"]*)" and "([^"]*)"')
def submit_login_credentials(context: Context, username: str, password: str) -> None:
    context.login_page.submit_login_credentials(username, password)


@then('User sees login form error')
def login_form_error(context: Context) -> None:
    context.login_page.login_form_error()


@then('User sees login notification error')
def login_notification_error(context: Context) -> None:
    context.login_page.login_notification_error()


@then('User is logged into his account')
def get_user_account(context: Context) -> None:
    context.login_page.get_user_account()
    context.login_page.user_logout()


@step('User logs out of the application')
def user_logout(context:Context) -> None:
    context.login_page.user_logout()
