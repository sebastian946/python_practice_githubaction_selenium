from behave import *
from stepsdefinition.loginsteps import *


loginPage = Login()
@given('user enter the source demo web page')
def step_impl(context):
    print('Esta aqui')
    loginPage.open_url()
    loginPage.get_text_user_credentials()
    loginPage.get_text_password_credentials()


@when(u'user enter the user {id} and password click login')
def step_impl(context,id):
    loginPage.send_user(id)


@then(u'show the login in the web page')
def step_impl(context):
    text_expect = loginPage.validate_login()
    print(text_expect)
    assert text_expect == "Swag Labs", False


@when(u'user enter the user {id} and login invalid')
def step_impl(context,id):
    loginPage.send_user(id)


@then(u'show message is incorrect the user and password')
def step_impl(context):
    text_expect = loginPage.validate_message_error()
    assert text_expect == "Epic sadface: Username and password do not match any user in this service", False