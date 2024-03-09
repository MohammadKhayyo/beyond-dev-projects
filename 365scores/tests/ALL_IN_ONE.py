import time
import unittest
import concurrent.futures
from SeleniumGridTest._365scores.infra.browser_wrapper import BrowserWrapper
from SeleniumGridTest._365scores.logic.logic import NavigationLogic
import sys


class GridTest(unittest.TestCase):

    def pytest_configure(config):
        # Force UTF-8 encoding for standard output and error.
        if sys.stdout.encoding != 'UTF-8':
            sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
        if sys.stderr.encoding != 'UTF-8':
            sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8', buffering=1)

    def setUp(self):
        pass

    def test_run_grid_parallel(self):
        """Executes tests in parallel across different browsers."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser_types)) as executor:
            futures = []
            for browser in self.browser_types:
                future = executor.submit(self.execute_test_with_caps, browser)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    self.fail(f"An error occurred during the tests: {e}")

    def execute_test_with_caps(self, browser_name):
        """Executes test for a specific browser, encapsulating setup and teardown."""
        self.pytest_configure()
        self.browser_wrapper = BrowserWrapper()
        driver = self.browser_wrapper.create_driver(browser_name)
        wait = self.browser_wrapper.get_wait(timeout=10)
        self.HUB_URL = self.browser_wrapper.config["hub"]
        self.browser_types = self.browser_wrapper.config["browser_types"]
        self.navigation_logic = NavigationLogic(driver, wait, self.browser_wrapper)

        try:
            # Sequence of test actions
            self.check_title()
            self.navigate_to_football_section()
            self.navigate_to_basketball_section()
            self.navigate_to_tennis_section()
            self.navigate_to_hockey_section()
        finally:
            self.browser_wrapper.close_browser()

    def check_title(self):
        """Checks the title of the homepage."""
        time.sleep(2)
        expected_url = self.browser_wrapper.config["url"]["english"]
        expected_title = "365Scores - Livescore, Results, Fixtures, News and Stats"
        actual_url, actual_title = self.navigation_logic.check_title(expected_url, expected_title)
        self.assertIn(expected_url, actual_url, "The page URL is not as expected.")
        self.assertEqual(actual_title, expected_title, "The homepage title does not match the expected value.")

    def navigate_to_football_section(self):
        """Navigates to the football section and checks the URL."""
        time.sleep(2)
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        expected_url = "https://www.365scores.com/he/football"
        actual_url = self.navigation_logic.navigate_to_section(url_to_navigate, "football", expected_url)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Football section correctly.")

    def navigate_to_basketball_section(self):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        expected_url = "https://www.365scores.com/he/basketball"
        actual_url = self.navigation_logic.navigate_to_section(url_to_navigate, "basketball", expected_url)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Basketball section correctly.")

    def navigate_to_tennis_section(self):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        expected_url = "https://www.365scores.com/he/tennis"
        actual_url = self.navigation_logic.navigate_to_section(url_to_navigate, "tennis", expected_url)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Tennis section correctly.")

    def navigate_to_hockey_section(self):
        """Navigates to the football section and checks the URL."""
        url_to_navigate = self.browser_wrapper.config["url"]["hebrew"]
        expected_url = "https://www.365scores.com/he/hockey"
        actual_url = self.navigation_logic.navigate_to_section(expected_url, "hockey", expected_url)
        self.assertIn(expected_url, actual_url, "Did not navigate to the Hockey section correctly.")
