from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventCreator:
    """Class to add an event in an application."""

    ADD_EVENT_BUTTON_XPATH = '//android.widget.ImageButton[@resource-id="com.claudivan.taskagenda:id/btNovoEvento"]'
    TOMORROW_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Tomorrow"]'
    TODAY_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Today"]'
    OTHER_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Other"]'
    EVENT_NAME_INPUT_XPATH = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etTitulo"]'
    EVENT_DESCRIPTION_INPUT_XPATH = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etDescricao"]'
    TASK_TYPE_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTipo"]'
    SAVE_TASK_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
    TASK_LIST_XPATH_TEMPLATE = '//android.widget.ListView[@resource-id="android:id/select_dialog_listview"]/android.widget.RelativeLayout[{}]'
    DATE_TEXT_VIEW_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/btData"]'

    def __init__(self, driver, event_name, description, task_number=1):
        """Initializes AddEvent with driver, event name, description, and task number."""
        self.driver = driver
        self.event_name = event_name
        self.description = description
        self.task_number = task_number

    def _wait_and_click(self, xpath):
        """Wait for an element to be clickable and then click."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def _find_and_send_keys(self, xpath, text):
        """Find an element and send keys to it."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_add_event(self):
        """Click the button to add a new event."""
        self._wait_and_click(self.ADD_EVENT_BUTTON_XPATH)

    def click_on_tomorrow(self):
        """Select 'Tomorrow' as the event date."""
        self._wait_and_click(self.TOMORROW_TEXTVIEW_XPATH)

    def click_on_today(self):
        """Select 'Tomorrow' as the event date."""
        self._wait_and_click(self.TODAY_TEXTVIEW_XPATH)

    def click_on_other(self):
        """Select 'Tomorrow' as the event date."""
        self._wait_and_click(self.OTHER_TEXTVIEW_XPATH)

    def enter_event_name(self):
        """Enter the event's name."""
        self._find_and_send_keys(self.EVENT_NAME_INPUT_XPATH, self.event_name)

    def enter_event_description(self):
        """Enter the event's description."""
        self._find_and_send_keys(self.EVENT_DESCRIPTION_INPUT_XPATH, self.description)

    def choose_task_type(self):
        """Choose the task type based on the provided task number."""
        self._wait_and_click(self.TASK_TYPE_TEXTVIEW_XPATH)
        task_xpath = self.TASK_LIST_XPATH_TEMPLATE.format(self.task_number)
        self._wait_and_click(task_xpath)

    def save_task(self):
        """Click the save button to add the task."""
        self._wait_and_click(self.SAVE_TASK_BUTTON_XPATH)

    def extract_day_number(self):
        """Extract the day number from a date string in a text element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.DATE_TEXT_VIEW_XPATH)))
        date_text = element.text
        day_number = date_text.split(',')[1].strip().split(' ')[0]
        return int(day_number)

    def add_task_flow(self, day='today'):
        """Perform the full flow to add a task."""
        self.click_on_add_event()
        if day == 'today':
            self.click_on_today()
        elif day == 'Tomorrow':
            self.click_on_tomorrow()
        elif day == 'other':
            self.click_on_other()
        day_number = self.extract_day_number()
        self.enter_event_name()
        self.enter_event_description()
        self.choose_task_type()
        self.save_task()
        return day_number
