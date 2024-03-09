import time
import unittest
import concurrent.futures

from selenium.webdriver.support.wait import WebDriverWait
from SeleniumGridTest._365scores.infra.browser_wrapper import BrowserWrapper
from SeleniumGridTest._365scores.logic.logic import NavigationLogic



class GridTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_run_grid_parallel(self):
        """Executes tests in parallel across different browsers."""
        self.browser_wrapper = BrowserWrapper()
        browsers = self.browser_wrapper.config["browser_types"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            futures = []
            for browser in browsers:
                future = executor.submit(self.execute_test_with_caps, browser)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    self.fail(f"An error occurred during the tests: {e}")

    def execute_test_with_caps(self, browser_name):
        """Executes test for a specific browser, encapsulating setup and teardown."""
        with self.browser_wrapper.driver_context(browser_name) as driver:
            # Increase the default wait time
            wait = WebDriverWait(driver, 10)  # Adjusted from 2 to 10 seconds
            driver.maximize_window()
            self.navigation_logic = NavigationLogic()

            # Proceed with test actions within the try block
            try:
                self.check_title(driver, wait)
                self.navigate_to_football_section(driver, wait)
                self.navigate_to_basketball_section(driver, wait)
                self.navigate_to_tennis_section(driver, wait)
                self.navigate_to_hockey_section(driver, wait)
            finally:
                pass  # driver.quit() is handled by the context manager

    def check_title(self, driver, wait):
        """Checks the title of the homepage."""
        expected_url = self.browser_wrapper.config["url"]["english"]
        self.browser_wrapper.navigate(driver, expected_url)
        expected_title = "365Scores - Livescore, Results, Fixtures, News and Stats"
        actual_url, actual_title = self.navigation_logic.check_title(expected_url, expected_title, driver, wait)
        self.assertIn(expected_url, actual_url, "The page URL is not as expected.")
        self.assertEqual(actual_title, expected_title, "The homepage title does not match the expected value.")

    def navigate_to_football_section(self, driver, wait):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        self.browser_wrapper.navigate(driver, url_to_navigate)
        expected_url = "https://www.365scores.com/he/football"
        actual_url = self.navigation_logic.navigate_to_section("football", expected_url, driver, wait)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Football section correctly.")

    def navigate_to_basketball_section(self, driver, wait):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        self.browser_wrapper.navigate(driver, url_to_navigate)
        expected_url = "https://www.365scores.com/he/basketball"
        actual_url = self.navigation_logic.navigate_to_section("basketball", expected_url, driver, wait)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Basketball section correctly.")

    def navigate_to_tennis_section(self, driver, wait):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        self.browser_wrapper.navigate(driver, url_to_navigate)
        expected_url = "https://www.365scores.com/he/tennis"
        actual_url = self.navigation_logic.navigate_to_section("tennis", expected_url, driver, wait)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Tennis section correctly.")

    def navigate_to_hockey_section(self, driver, wait):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        self.browser_wrapper.navigate(driver, url_to_navigate)
        expected_url = "https://www.365scores.com/he/hockey"
        actual_url = self.navigation_logic.navigate_to_section("hockey", expected_url, driver, wait)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Hockey section correctly.")
