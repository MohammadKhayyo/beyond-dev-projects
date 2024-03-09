from SeleniumGridTest._365scores.infra.page_base import PageBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NavigationLogic(PageBase):
    NOTICE_AGREE_BUTTON = (By.XPATH, '//button[@id="didomi-notice-agree-button"]')
    SVG = "//div/*[local-name()='svg' and @viewBox='0 0 24 24']/*[local-name()='path' and @d = 'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z']"
    ENUM = {
        'football': "//button[.//div[text()='כדורגל']]",
        'basketball': "//button[.//div[text()='כדורסל']]",
        'tennis': "//button[.//div[text()='טניס']]",
        'hockey': "//button[.//div[text()='הוקי']]"
    }

    def __init__(self):
        super().__init__()

    def check_title(self, expected_url, expected_title, driver, wait):
        """Checks the page title and URL after navigating to the expected URL."""
        wait.until(lambda driver: expected_url == driver.current_url)
        wait.until(lambda driver: expected_title == driver.title)
        wait.until(EC.title_is(expected_title))
        actual_url = driver.current_url
        actual_title = driver.title
        return actual_url, actual_title

    def try_clicking_element(self, primary_xpath, fallback_xpath, driver):
        wait = WebDriverWait(driver, 5)  # Wait up to 5 seconds
        try:
            wait.until(
                EC.element_to_be_clickable(self.NOTICE_AGREE_BUTTON)).click()
        except Exception as E:
            print(E)
        try:
            wait.until(
                EC.element_to_be_clickable((By.XPATH, primary_xpath))).click()
        except Exception as E:
            print(E)
            wait.until(
                EC.element_to_be_clickable((By.XPATH, fallback_xpath))).click()
            wait.until(
                EC.element_to_be_clickable((By.XPATH, primary_xpath))).click()

    def navigate_to_section(self, section, expected_url, driver, wait):
        """Navigates to a specific section of the site and verifies the URL."""
        self.try_clicking_element(self.ENUM[section], self.SVG, driver)
        wait.until(lambda driver: expected_url == driver.current_url)
        current_url = driver.current_url
        return current_url
