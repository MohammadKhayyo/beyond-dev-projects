import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ThemeColorChanger:
    """Class to change the theme color in an application."""

    SETTINGS_XPATH = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
    COLOR_SETTING_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btCores"]'
    MAIN_COLOR_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/item_background"]'
    Pink_COLOR_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/container_cores"]/android.widget.LinearLayout[5]/android.view.View[1]'
    SAVE_CHANGES_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
    PERMISSION_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'

    def __init__(self, driver):
        self.driver = driver

    def _find_element_and_click(self, xpath):
        """Finds an element by its XPath and clicks it."""
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def open_settings(self):
        """Finds the settings icon and clicks."""
        self._find_element_and_click(self.SETTINGS_XPATH)

    def access_color_settings(self):
        """Finds and clicks the color settings option."""
        self._find_element_and_click(self.COLOR_SETTING_XPATH)

    def select_main_color(self):
        """Finds and clicks the main color option to change the theme."""
        self._find_element_and_click(self.MAIN_COLOR_XPATH)

    def pick_pink_color(self):
        """Selects a new color for the theme."""
        self._find_element_and_click(self.Pink_COLOR_XPATH)

    def save_theme_changes(self):
        """Saves the changes made to the theme color."""
        self._find_element_and_click(self.SAVE_CHANGES_XPATH)

    def dismiss_permission_prompt(self):
        """Handles the permission button if it appears."""
        try:
            self._find_element_and_click(self.PERMISSION_BUTTON_XPATH)
        except NoSuchElementException:
            pass  # If the element is not found, do nothing

    def update_theme_color(self):
        """Executes the overall process to change the theme color."""
        self.open_settings()
        time.sleep(1)
        self.access_color_settings()
        time.sleep(1)
        self.select_main_color()
        self.pick_pink_color()
        self.save_theme_changes()
        self.dismiss_permission_prompt()
        return True
