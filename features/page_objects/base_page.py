from typing import Tuple
from faker import Faker

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()


class BasePage:
    def __init__(self, browser) -> None:
        self.base_url = "https://www.fitatu.com/"
        self.browser = browser

    login_link = (By.CSS_SELECTOR, '.menu--desktop a:last-child')
    rodo_button = (By.CSS_SELECTOR, '.rodo-notification__button')

    def visit(self) -> None:
        self.browser.get(self.base_url)

    def find_element(self, *locator: Tuple) -> WebElement:
        return self.browser.find_element(*locator)

    def get_current_url(self) -> str:
        return self.browser.current_url

    def wait_for_element(self, *locator: Tuple) -> None:
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(*locator)
        )

    @staticmethod
    def generate_fake_email() -> str:
        return fake.email()

    @staticmethod
    def generate_fake_password() -> str:
        return fake.password()
