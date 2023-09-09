from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert "unregistered@yahoo.com" email')
def step_impl(context):
    context.login_page.insert_invalid_email()


@when("I insert a password")
def step_impl(context):
    context.login_page.insert_some_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("Main error is displayed")
def step_impl(context):
    context.login_page.check_error()


