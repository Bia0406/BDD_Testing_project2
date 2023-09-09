from browser import Browser
from pages.login_page import LoginPage


def before_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    inainte rularii tuturor pasiilor
    """
    context.browser = Browser()
    context.login_page = LoginPage()


def after_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    dupa rularea tuturor pasiilor
    """
    context.browser.close()
