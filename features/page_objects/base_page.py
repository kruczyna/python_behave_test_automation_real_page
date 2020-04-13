from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser) -> None:
        self.base_url = "https://www.fitatu.com/"
        self.browser = browser

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
