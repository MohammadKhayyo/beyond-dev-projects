from dsl.dsl import DSL
from selenium.webdriver.common.by import By


class Login_Page:
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.dsl = DSL(driver)

    def set_login(self, username):
        self.dsl.insert_text_by_id(self.USER_NAME_INPUT[1], username)

    def set_password(self, password):
        self.dsl.insert_text_by_id(self.PASSWORD_INPUT[1], password)

    def click_login_button(self):
        self.dsl.click_element_by_id(self.LOGIN_BUTTON[1])

    def complete_login(self, username, password):
        self.dsl.insert_text_by_id(self.USER_NAME_INPUT[1], username)
        self.dsl.insert_text_by_id(self.PASSWORD_INPUT[1], password)
        self.dsl.click_element_by_id(self.LOGIN_BUTTON[1])
