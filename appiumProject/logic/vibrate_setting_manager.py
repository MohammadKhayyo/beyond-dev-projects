import time
from selenium.webdriver.common.by import By


class VibrateSettingManager:
    """Class to interact with the vibrate settings of an app."""

    ICON_SETTINGS_XPATH = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
    TEXTVIEW_GENERAL_SETTINGS_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvAjustes"]'
    TEXTVIEW_ALERTS_NOTIFICATIONS_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvAlarmesENotificacoes"]'
    SWITCH_VIBRATE_XPATH = '//android.widget.Switch[@resource-id="com.claudivan.taskagenda:id/swVibracaoAlarmeEvento"]'

    def __init__(self, driver):
        """Initializes the VibrateFeature with a Selenium WebDriver."""
        self.driver = driver
        self.previous_state = None
        self.current_state = None

    def _wait_for_element_and_click(self, xpath):
        """Finds an element using XPath and clicks it."""
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(1)  # Wait for UI to respond to the click.

    def navigate_to_settings(self):
        """Finds the settings icon and clicks it three times."""
        self._wait_for_element_and_click(self.ICON_SETTINGS_XPATH)

    def access_general_settings(self):
        """Finds and clicks the overall settings."""
        self._wait_for_element_and_click(self.TEXTVIEW_GENERAL_SETTINGS_XPATH)

    def open_alerts_and_notifications(self):
        """Finds and clicks the alarms and notifications setting."""
        self._wait_for_element_and_click(self.TEXTVIEW_ALERTS_NOTIFICATIONS_XPATH)

    def toggle_vibrate_option(self):
        """Clicks on the vibrate switch and stores the old and new state."""
        element = self.driver.find_element(By.XPATH, self.SWITCH_VIBRATE_XPATH)
        self.previous_state = element.get_attribute("checked") == "true"
        element.click()
        time.sleep(1)
        self.current_state = element.get_attribute("checked") == "true"

    def modify_vibration_setting(self):
        """Executes the process to change the vibrate setting and returns the old and new states."""
        self.navigate_to_settings()
        self.access_general_settings()
        self.open_alerts_and_notifications()
        self.toggle_vibrate_option()
        return [self.previous_state, self.current_state]
