from dsl.dsl import DSL
from selenium.webdriver.common.by import By

import re


class Checkout_Page:
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    SUMMARY_SUBTOTAL_LABEL = (By.CLASS_NAME, 'summary_subtotal_label')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')
    TITLE = (By.CLASS_NAME, 'title')

    def __init__(self, driver):
        self.dsl = DSL(driver)

    def set_first_name(self, first_name):
        self.dsl.insert_text_by_id(self.FIRST_NAME_INPUT[1], first_name)

    def set_last_name(self, last_name):
        self.dsl.insert_text_by_id(self.LAST_NAME_INPUT[1], last_name)

    def set_zip_postal_code(self, zip_postal_code):
        self.dsl.insert_text_by_id(self.ZIP_POSTAL_CODE_INPUT[1], zip_postal_code)

    def continue_to_checkout_overview(self):
        self.dsl.click_element_by_id(self.CONTINUE_BUTTON[1])

    def fulfill_checkout_information(self, first_name, last_name, zip_postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_zip_postal_code(zip_postal_code)
        self._continue_to_checkout_overview()

    def _continue_to_checkout_overview(self):
        self.dsl.click_element_by_id(self.CONTINUE_BUTTON[1])

    def get_total_value(self):
        text_n_value = self.dsl.get_text_by_class(self.SUMMARY_SUBTOTAL_LABEL[1])
        value = float(re.search(r'\d+\.\d+', text_n_value).group())
        return value

    def finish_overview(self):
        self.dsl.click_element_by_id(self.FINISH_BUTTON[1])

    def get_checkout_status_message(self):
        self.dsl.get_text_by_class(self.TITLE[1])

    def get_checkout_complete_message(self):
        self.dsl.get_text_by_class(self.COMPLETE_HEADER[1])
