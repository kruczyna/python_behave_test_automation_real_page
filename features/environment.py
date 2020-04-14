from selenium import webdriver

from features.page_objects.login_page import LoginPage
from features.page_objects.registration_page import RegistrationPage
from features.page_objects.register_profile_page import RegisterProfilePage


def before_all(context):
    context.driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromedriver'
    )
    context.login_page = LoginPage(context.driver)
    context.register_page = RegistrationPage(context.driver)
    context.register_profile_page = RegisterProfilePage(context.driver)

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)


def after_all(context):
    context.driver.quit()
