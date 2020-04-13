from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from features.page_objects.base_page import BasePage


class LoginPage(BasePage):
    login_button = (By.CSS_SELECTOR, '.page-login__submit-button')
    username_field = (By.CSS_SELECTOR, '#username')
    username_field_error = (By.CSS_SELECTOR, '#username + div.input-base__validation-error-message')
    password_field = (By.CSS_SELECTOR, '#password')
    password_field_error = (By.CSS_SELECTOR, '#password + div.input-base__validation-error-message')
    incorrect_credentials_notification = (By.CSS_SELECTOR, '.notification--error')
    user_email = (By.CSS_SELECTOR, '.menu__user')
    logout_link = (By.CSS_SELECTOR, 'div.menu__list-container > ul > a:nth-child(3)')

    def navigate_to_login_form(self) -> None:
        self.visit()
        self.find_element(*self.login_link).click()
        self.wait_for_element(self.password_field)
        self.wait_for_element(self.username_field)
        assert "login" in self.get_current_url()

    def submit_login_credentials(self, username: str, password: str) -> None:
        self.find_element(*self.username_field).send_keys(username)
        self.find_element(*self.password_field).send_keys(password)
        self.find_element(*self.login_button).click()

    def login_form_error(self) -> None:
        try:
            self.wait_for_element(self.username_field_error)
        except TimeoutException:
            self.wait_for_element(self.password_field_error)

    def login_notification_error(self) -> None:
        self.wait_for_element(self.incorrect_credentials_notification)

    def get_user_account(self) -> None:
        self.find_element(*self.user_email)
        self.find_element(*self.logout_link)
        self.wait_for_url("profile-settings")

    def user_logout(self) -> None:
        self.find_element(*self.logout_link).click()
