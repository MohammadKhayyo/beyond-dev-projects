from dsl.dsl import DSL
from selenium.webdriver.common.by import By


class Inventory_Page:
    # Global locators for elements on the inventory page
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.XPATH, '//select[@data-test="product_sort_container"]')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="checkout"]')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    ADD_TO_CART_BUTTONS = (By.XPATH, '//div[@class="inventory_item"]//button')
    REACT_BURGER_MENU_BTN = (By.ID, 'react-burger-menu-btn')
    RESET_SIDEBAR_LINK = (By.ID, 'reset_sidebar_link')
    REACT_BURGER_CROSS_BTN = (By.ID, 'react-burger-cross-btn')

    def __init__(self, driver):
        self.dsl = DSL(driver)

    def get_inventory_items_titles(self):
        return self.dsl.get_items_titles(self.INVENTORY_ITEM_NAME[1])

    def get_inventory_item_title_by_index(self, index):
        return self.dsl.get_items_titles(self.INVENTORY_ITEM_NAME[1])[index]

    def get_inventory_items_prices(self):
        return self.dsl.get_items_prices(self.INVENTORY_ITEM_PRICE[1])

    def get_inventory_item_price_by_index(self, index):
        return self.dsl.get_items_prices(self.INVENTORY_ITEM_PRICE[1])[index]

    def add_item_to_cart_by_index(self, index):
        self.dsl.get_buttons_list_by_xpath(self.ADD_TO_CART_BUTTONS[1])[index].click()

    def select_sort_type_by_text(self, visible_text_option):
        self.dsl.select_by_visible_text(self.SORT_DROPDOWN[1], visible_text_option)

    def get_sort_type_text(self):
        return self.dsl.get_visible_text_selected(self.SORT_DROPDOWN[1])

    def reset_app_state(self):
        self.dsl.click_element_by_id(self.REACT_BURGER_MENU_BTN[1])
        self.dsl.click_element_by_id(self.RESET_SIDEBAR_LINK[1])
        self.dsl.click_element_by_id(self.REACT_BURGER_CROSS_BTN[1])

    def access_cart(self):
        self.dsl.click_element_by_class(self.CART_BUTTON[1])

    def go_to_checkout(self):
        self.dsl.click_element_by_xpath(self.CHECKOUT_BUTTON[1])

    # checkout
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
        self.continue_to_checkout_overview()
