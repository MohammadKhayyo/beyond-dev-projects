from selenium.webdriver.common.by import By


class CheckArrows:
    """Class to check functionality of next and previous arrows in an app."""

    DATE_VIEW_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvVisor"]'
    RIGHT_ARROW_XPATH = '(//android.widget.ImageView[@content-desc="Image"])[2]'
    LEFT_ARROW_XPATH = '(//android.widget.ImageView[@content-desc="Image"])[1]'

    def __init__(self, driver):
        """Initializes CheckArrows with a driver."""
        self.driver = driver
        self.old_date = ""
        self.new_date = ""

    def _save_date(self, attribute):
        """Saves the date displayed in the app to an attribute."""
        element = self.driver.find_element(By.XPATH, self.DATE_VIEW_XPATH)
        setattr(self, attribute, element.get_attribute('text'))

    def _press_arrow(self, arrow_xpath):
        """Presses an arrow based on the provided XPath."""
        element = self.driver.find_element(By.XPATH, arrow_xpath)
        element.click()

    def _parse_date(self, date_string):
        """Parses the date string and extracts the start day."""
        # Example input: "3/Mar - 9/Mar" or "10/Mar - 16/Mar"
        start_day = date_string.split('/')[0]
        return int(start_day)

    def arrows_flow(self, flag):
        """Performs the arrow press flow and calculates the difference in dates."""
        self._save_date('old_date')

        if flag == "next":
            self._press_arrow(self.RIGHT_ARROW_XPATH)
        elif flag == "prev":
            self._press_arrow(self.LEFT_ARROW_XPATH)
        else:
            raise ValueError("Invalid flag value. Use 'next' or 'prev'.")

        self._save_date('new_date')

        # Parse the dates to extract the start day
        first_number = self._parse_date(self.old_date)
        second_number = self._parse_date(self.new_date)

        # Calculate the difference
        return abs(first_number - second_number)
