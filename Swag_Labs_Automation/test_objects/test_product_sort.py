from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from page_objects.login_page import Login_Page
from page_objects.inventory_page import Inventory_Page


class Test_Product(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = Login_Page(self.driver)
        self.login_page.complete_login("standard_user", "secret_sauce")
        self.inventory_page = Inventory_Page(self.driver)

    def test_default_sort(self):
        items_titles = self.inventory_page.get_inventory_items_titles()
        sorted_items_titles = items_titles.copy()
        sorted_items_titles.sort()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Name (A to Z)', 'Default order is not correct.')
        self.assertListEqual(items_titles, sorted_items_titles, "Items are not correctly ordered.")

    def test_invert_named_sort(self):
        self.inventory_page.select_sort_type_by_text('Name (Z to A)')

        items_titles = self.inventory_page.get_inventory_items_titles()
        reverse_sorted_items_titles = items_titles.copy()
        reverse_sorted_items_titles.sort()
        reverse_sorted_items_titles.reverse()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Name (Z to A)', 'Selected order is not correct.')
        self.assertListEqual(items_titles, reverse_sorted_items_titles, "Items are not correctly ordered.")

    def test_sort_price_low_high(self):
        self.inventory_page.select_sort_type_by_text('Price (low to high)')

        items_prices = self.inventory_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Price (low to high)',
                         'Order is not the selected one.')
        self.assertListEqual(items_prices, sorted_items_prices,
                             "Items are not correctly ordered by price (low to high).")

    def test_sort_price_high_low(self):
        self.inventory_page.select_sort_type_by_text('Price (high to low)')

        items_prices = self.inventory_page.get_inventory_items_prices()
        sorted_reverse_items_prices = items_prices.copy()
        sorted_reverse_items_prices.sort()
        sorted_reverse_items_prices.reverse()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Price (high to low)',
                         'Order is not the selected one.')
        self.assertListEqual(items_prices, sorted_reverse_items_prices,
                             "Items are not correctly ordered by price (high to low).")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
