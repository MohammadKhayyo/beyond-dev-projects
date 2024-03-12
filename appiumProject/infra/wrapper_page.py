from appium import webdriver
from appium.options.android import UiAutomator2Options
from infra.config_reader import ConfigurationManager


class BasePage:
    URL = 'http://localhost:4723'

    def __init__(self):
        self.configuration_manager = ConfigurationManager()
        self.capabilities = self.configuration_manager.load_settings()
        self.capabilities_options = UiAutomator2Options().load_capabilities(self.capabilities)
        self.driver = webdriver.Remote(
            command_executor=self.URL,
            options=self.capabilities_options
        )

    def driver_set_up(self):
        return self.driver
