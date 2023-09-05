from browser import Browser


def before_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    inainte rularii tuturor pasiilor
    """
    context.browser = Browser()


def after_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    dupa rularea tuturor pasiilor
    """
    context.browser.close()
