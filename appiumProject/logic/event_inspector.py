from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class XPathConstants:
    """Class to store all the XPaths as global variables."""
    SETTINGS_ICON_XPATH = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
    ALL_EVENTS_BUTTON_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btEventos"]'
    PERMISSION_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
    CALENDAR_BUTTON_XPATH = '//android.widget.LinearLayout[@content-desc="Calendar"]'
    EVENT_TITLE_XPATH = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTitulo"]'
    DELETE_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_excluir"]'
    CONFIRM_DELETE_BUTTON_XPATH = '//android.widget.Button[@resource-id="android:id/button1"]'
    CANCEL_DELETE_BUTTON_XPATH = '//android.widget.Button[@resource-id="android:id/button2"]'
    EDIT_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_editar"]'
    EVENT_NAME_INPUT_XPATH = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etTitulo"]'
    SAVE_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'


class EventInspector:
    """Class to interact with event list and related actions in an app."""

    def __init__(self, driver, event_name):
        self.driver = driver
        self.event_name = event_name

    def _wait_and_click(self, xpath):
        """Wait for an element to be clickable and then click."""
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def find_settings(self):
        """Press on the settings icon three times."""
        self._wait_and_click(XPathConstants.SETTINGS_ICON_XPATH)

    def press_on_all_events(self):
        """Press on the all events button."""
        self._wait_and_click(XPathConstants.ALL_EVENTS_BUTTON_XPATH)

    def handle_permission_button(self):
        """Handle the permission button if it appears."""
        try:
            self._wait_and_click(XPathConstants.PERMISSION_BUTTON_XPATH)
        except:
            pass

    def check_event(self, newName=None):
        if newName is None:
            newName = self.event_name
        try:
            text_views = self.driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            for text_view in text_views:
                text = text_view.text.strip()
                if text.lower() == newName.lower():
                    print("Found", newName, " in a TextView:", text_view.get_attribute("resource-id"))
                    return True
            return False
        except:
            return False

    def verify_flow(self):
        self.find_settings()
        self.press_on_all_events()
        self.handle_permission_button()
        return self.check_event()

    def open_calendar(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.CALENDAR_BUTTON_XPATH)
        element.click()

    def click_on_date(self, day_number):
        """Click on the date on the calendar."""
        date_xpath = f'//android.widget.TextView[@text="{day_number}"]'
        self._wait_and_click(date_xpath)

    def verify_flow_calendar(self, day_number):
        self.open_calendar()
        self.click_on_date(day_number)
        self.handle_permission_button()
        final_res = self.check_event()
        return final_res

    def press_on_date_on_week_page(self, day_number):
        element_xpath = f'//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/dia_mes" and @text="{day_number}"]'
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def verify_flow_week(self, day_number):
        self.press_on_date_on_week_page(day_number)
        self.handle_permission_button()
        final_res = self.check_event()
        return final_res

    def press_on_event(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.EVENT_TITLE_XPATH)
        element.click()

    def press_on_delete(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.DELETE_BUTTON_XPATH)
        element.click()

    def delete_confirm(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.CONFIRM_DELETE_BUTTON_XPATH)
        element.click()

    def not_delete_confirm(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.CANCEL_DELETE_BUTTON_XPATH)
        element.click()

    def verify_delete_flow(self):
        self.find_settings()
        self.press_on_all_events()
        self.handle_permission_button()
        self.press_on_event()
        self.press_on_delete()
        self.delete_confirm()
        final_res = self.check_event()
        return final_res

    def verify_not_delete_flow(self):
        self.find_settings()
        self.press_on_all_events()
        self.handle_permission_button()
        self.press_on_event()
        self.press_on_delete()
        self.not_delete_confirm()
        final_res = self.check_event()
        return final_res

    def press_on_edit(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.EDIT_BUTTON_XPATH)
        element.click()

    def modify_event_name(self, newName):
        element = self.driver.find_element(By.XPATH, XPathConstants.EVENT_NAME_INPUT_XPATH)
        element.clear()
        element.send_keys(newName)

    def click_on_save(self):
        element = self.driver.find_element(By.XPATH, XPathConstants.SAVE_BUTTON_XPATH)
        element.click()

    def verify_modify_flow(self, newName):
        self.find_settings()
        self.press_on_all_events()
        self.handle_permission_button()
        self.press_on_event()
        self.press_on_edit()
        self.modify_event_name(newName)
        self.click_on_save()
        final_res = self.check_event(newName)
        return final_res
