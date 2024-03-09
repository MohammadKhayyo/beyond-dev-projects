from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from .config_loader import ConfigLoader
from selenium.common.exceptions import WebDriverException
from contextlib import contextmanager


class BrowserWrapper:
    def __init__(self):
        self.config = ConfigLoader.load_config()

    def create_driver(self, browser_name):
        """Creates a WebDriver instance based on browser options."""
        browser_options = self.get_browser_options(browser_name)
        hub_url = self.config.get("hub")
        if self.config.get("grid"):
            try:
                driver = webdriver.Remote(command_executor=hub_url, options=browser_options)
                return driver
            except WebDriverException as e:
                print(f"Failed to create WebDriver session: {e}")
                raise
        else:
            raise ValueError("Grid support is not configured.")

    def get_browser_options(self, browser_name):
        """Returns browser options for the specified browser."""
        if browser_name == 'chrome':
            return webdriver.ChromeOptions()
        elif browser_name == 'firefox':
            return webdriver.FirefoxOptions()
        elif browser_name == 'edge':
            return webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    @contextmanager
    def driver_context(self, browser_name):
        driver = self.create_driver(browser_name)
        try:
            yield driver
        finally:
            if driver is not None:
                driver.quit()

    def get_wait(self, driver, timeout=10):
        """Returns a WebDriverWait object for the specified driver."""
        return WebDriverWait(driver, timeout)

    def navigate(self, driver, url):
        """Navigates to a specified URL using the given driver."""
        driver.get(url)
        self.get_wait(driver, 10).until(lambda driver: url == driver.current_url)
