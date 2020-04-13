from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from features.page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    register_button = (By.CSS_SELECTOR, '.page-login__register-button')
    email_field = (By.CSS_SELECTOR, 'input[type="email"]')
    email_field_error = (By.CSS_SELECTOR, 'input[type="email"] + span.validation__message')
    password_field = (By.CSS_SELECTOR, 'input[type="password"]')
    password_field_error = (By.CSS_SELECTOR, 'input[type="password"] + span.validation__message')
    terms_and_conditions_agreement_checkbox = (By.CSS_SELECTOR, 'div[data-key="acceptTerms"]')
    age_requirements_agreement_checkbox = (By.CSS_SELECTOR, 'div[data-key="acceptAgeRequirements"]')
    sensitive_data_agreement_checkbox = (By.CSS_SELECTOR, 'div[data-key="sensitiveAccepted"]')
    marketing_agreement_checkbox = (By.CSS_SELECTOR, 'div[data-key="marketingAccepted"]')
    create_account_button = (By.CSS_SELECTOR, '.create-new-account-page__register-button')
    subscription_plan = (By.CSS_SELECTOR, '.subscription-select__plan')

    @staticmethod
    def get_agreement_error(agreement_selector):
        return By.CSS_SELECTOR, f"{agreement_selector}[class*='checkbox--validation-error']"

    def navigate_to_register_form(self) -> None:
        self.visit()
        self.find_element(*self.login_link).click()
        assert "login" in self.get_current_url()
        self.find_element(*self.register_button).click()
        self.wait_for_element(self.password_field)
        self.wait_for_element(self.email_field)
        assert "create-account" in self.get_current_url()

    def submit_empty_register_form(self) -> None:
        self.find_element(*self.rodo_button).click()
        self.find_element(*self.create_account_button).click()

    def get_required_register_fields(self) -> None:
        self.find_element(*self.email_field_error)
        self.find_element(*self.password_field_error)
        self.get_agreement_error(self.age_requirements_agreement_checkbox)
        self.get_agreement_error(self.sensitive_data_agreement_checkbox)
        self.get_agreement_error(self.terms_and_conditions_agreement_checkbox)

    def accept_agreements_checkoboxes(self) -> None:
        self.find_element(*self.terms_and_conditions_agreement_checkbox).click()
        self.find_element(*self.age_requirements_agreement_checkbox).click()
        self.find_element(*self.sensitive_data_agreement_checkbox).click()

    def input_invalid_register_credentials(self, email: str, password: str) -> None:
        self.find_element(*self.email_field).send_keys(email)
        self.find_element(*self.password_field).send_keys(password)

    def get_register_form_error(self) -> None:
        try:
            self.wait_for_element(self.email_field)
        except TimeoutException:
            self.wait_for_element(self.password_field_error)

    def submit_register_form(self) -> None:
        self.find_element(*self.email_field).send_keys(self.generate_fake_email())
        self.find_element(*self.password_field).send_keys(self.generate_fake_password())
        self.find_element(*self.create_account_button).click()

    def navigate_to_profile_settings(self) -> None:
        self.wait_for_element(self.subscription_plan)
        assert "order-and-payment" in self.get_current_url()
