from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_IN = (By.CLASS_NAME, "ico-login")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MSG = (By.CLASS_NAME, 'message-error')

    def navigate_to_login_page(self):
        self.browser.get(self._BASE_URL)
        login_in = self.find(*self.LOGIN_IN)
        self.click(login_in)

    def insert_invalid_email(self):
        email = self.find(*self.EMAIL)
        self.insert(email, "unregistered@yahoo.com")

    def insert_some_password(self):
        password = self.find(*self.PASSWORD)
        self.insert(password, "123456")

    def click_login_button(self):
        login_btn = self.find(*self.LOGIN_BUTTON)
        self.click(login_btn)

    def check_error(self):
        error_msg = self.find(*self.ERROR_MSG)
        actual_error = error_msg.text
        assert error_msg == actual_error


