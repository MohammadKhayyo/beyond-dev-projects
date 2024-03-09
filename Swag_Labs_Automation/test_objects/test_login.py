from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from page_objects.login_page import Login_Page


class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = Login_Page(self.driver)

    def test_login_locked(self):
        self.login_page.complete_login("locked_out_user", "secret_sauce")

        self.assertEqual(
            self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text,
            "Epic sadface: Sorry, this user has been locked out.",
            "Error message of locked user is incorrect."
        )

    def test_login_pass(self):
        self.login_page.complete_login("standard_user", "secret_sauce")

        self.assertEqual(
            self.driver.find_element(By.XPATH, '//div[@class="app_logo"]').text,
            "Swag Labs",
            "App name is not displayed correctly."
        )

        self.assertEqual(
            self.driver.current_url,
            'https://www.saucedemo.com/inventory.html',
            'Login did not redirect correctly.'
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
