from selenium import webdriver

from features.page_objects.login_page import LoginPage


def before_all(context):
    context.driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromedriver'
    )
    context.login_page = LoginPage(context.driver)

    context.driver.implicitly_wait(6)


def after_all(context):
    context.driver.quit()
