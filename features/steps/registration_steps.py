from behave import given, when, then
from behave.runner import Context


@given('User navigates to registration form')
def navigate_to_register_form(context: Context) -> None:
    context.register_page.navigate_to_register_form()


@when('User submits an empty registration form')
def submit_empty_register_form(context: Context) -> None:
    context.register_page.submit_empty_register_form()


@then('User sees which fields are required')
def get_required_register_fields(context: Context) -> None:
    context.register_page.get_required_register_fields()


@when('User inputs invalidly formatted "{email}" and "{password}"')
def input_invalid_register_credentials(context: Context, email: str, password: str) -> None:
    context.register_page.input_invalid_register_credentials(email, password)


@then('User sees register form validation error')
def get_register_form_error(context: Context) -> None:
    context.register_page.get_register_form_error()


@when('User submits valid register credentials')
def submit_register_form(context: Context) -> None:
