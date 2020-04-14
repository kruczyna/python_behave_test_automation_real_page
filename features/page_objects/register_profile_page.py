from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from features.page_objects.base_page import BasePage


class RegisterProfilePage(BasePage):
    date_of_birth_datepicker = (By.CSS_SELECTOR, '.vdp-datepicker')
    height_input = (By.CSS_SELECTOR, 'input[name="height"][data-validation-message="120 - 219 cm"]')
    height_input_error = (By.CSS_SELECTOR, 'label[class*="js--validation-error"][data-labeled-input-unit="cm"]')
    body_weight_input = (By.CSS_SELECTOR, 'div:nth-child(6) > div > div:nth-child(1) > div.switch-form__unit--active '
                                          '> label > input')
    body_weight_input_error = (By.CSS_SELECTOR, 'div:nth-child(6) > div > div:nth-child(1) > '
                                                'div.switch-form__unit--active > label.validation__container--error')
    goal_weight_input = (By.CSS_SELECTOR, 'div:nth-child(7) > div > div:nth-child(1) > div.switch-form__unit--active '
                                          '> label > input')
    goal_weight_input_error = (By.CSS_SELECTOR, 'div:nth-child(7) > div > div:nth-child(1) > '
                                                'div.switch-form__unit--active > label.validation__container--error')
    submit_profile = (By.CSS_SELECTOR, '.initial-profile-settings-page__submit-button')
    progress_loader = (By.CSS_SELECTOR, '.progress-loader__bar')
    process_description = (By.CSS_SELECTOR, '.process-start__description')

    def submit_initial_profile(self) -> None:
        element = self.find_element(*self.submit_profile)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        self.find_element(*self.submit_profile).click()

    def get_initial_profile_settings_error(self) -> None:
        self.wait_for_element(self.height_input_error)
        self.wait_for_element(self.body_weight_input_error)
        self.wait_for_element(self.goal_weight_input_error)

    def submit_initial_profile_with_min_data(self, heigth: str, current_weigth: str, goal_weigth: str) -> None:
        self.page_has_loaded()
        self.wait_for_element(self.goal_weight_input)
        self.wait_for_element(self.height_input)
        self.wait_for_element(self.body_weight_input)
        rgb = self.find_element(*self.progress_loader).value_of_css_property("background-color")
        color = Color.from_string(rgb).hex
        self.find_element(*self.height_input).send_keys(heigth)
        self.find_element(*self.body_weight_input).send_keys(current_weigth)
        self.find_element(*self.goal_weight_input).send_keys(goal_weigth)
        self.submit_initial_profile()

    def navigate_to_thank_you_page(self) -> None:
        self.wait_for_element(self.process_description)
        self.wait_for_element()
        assert "matching-process-start" in self.get_current_url()
