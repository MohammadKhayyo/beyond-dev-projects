from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DSL:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def insert_text_by_id(self, id_locator, text):
        self.driver.find_element(By.ID, id_locator).send_keys(text)

    def click_element_by_id(self, id_locator):
        element_to_be_clicked = self.driver.find_element(By.ID, id_locator)
        self.wait.until(EC.element_to_be_clickable(element_to_be_clicked))
        element_to_be_clicked.click()

    def click_element_by_class(self, class_locator):
        self.driver.find_element(By.CLASS_NAME, class_locator).click()

    def click_element_by_xpath(self, xpath_locator):
        self.driver.find_element(By.XPATH, xpath_locator).click()

    # Inventory page
    def get_items_titles(self, class_locator):
        items_titles = []
        for item_title in self.driver.find_elements(By.CLASS_NAME, class_locator):
            items_titles.append(item_title.text)
        return items_titles

    def get_items_prices(self, class_locator):
        items_prices = []
        for item_price in self.driver.find_elements(By.CLASS_NAME, class_locator):
            only_numbers = item_price.text.replace('$', '')
            items_prices.append(float(only_numbers))
        return items_prices

    def get_buttons_list_by_xpath(self, xpath_locator):
        return self.driver.find_elements(By.XPATH, xpath_locator)

    def select_by_visible_text(self, xpath_locator, visible_text):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        select.select_by_visible_text(visible_text)

    def get_visible_text_selected(self, xpath_locator):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        return select.first_selected_option.text

    # checkout
    def get_text_by_class(self, class_locator):
        return self.driver.find_element(By.CLASS_NAME, class_locator).text



