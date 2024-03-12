from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventTypeCreator:
    """Class to add a new event type in an application."""

    SETTINGS_ICON_XPATH = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
    TYPE_SETTING_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btCores"]'
    ADD_NEW_TYPE_BUTTON_XPATH = '//android.widget.TextView[@text="Add new"]'
    TYPE_NAME_INPUT_XPATH = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etNome"]'
    TYPE_COLOR_VIEW_XPATH = '//android.view.View[@resource-id="com.claudivan.taskagenda:id/cvCor"]'
    SELECTED_TYPE_COLOR_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/container_cores"]/android.widget.LinearLayout[5]/android.view.View[2]'
    TYPE_ICON_IMAGE_XPATH = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/ivIcone"]'
    SELECTED_TYPE_ICON_XPATH = '(//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/ivIcone"])[18]'
    OK_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_ok"]'
    SAVE_CHANGES_BUTTON_XPATH = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
    HOME_BUTTON_XPATH = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/containerColunasHorarios"]/android.widget.RelativeLayout[7]'

    def __init__(self, driver, event_type_name):
        self.driver = driver
        self.event_type_name = event_type_name

    def _click(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def _write_and_submit(self, xpath, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()
        element.clear()
        element.send_keys(text)

    def find_settings(self):
        for _ in range(3):
            self._click(self.SETTINGS_ICON_XPATH)

    def find_type_setting(self):
        self._click(self.TYPE_SETTING_XPATH)

    def find_new_type_button(self):
        self._click(self.ADD_NEW_TYPE_BUTTON_XPATH)

    def write_type_name(self):
        self._write_and_submit(self.TYPE_NAME_INPUT_XPATH, self.event_type_name)

    def choose_type_color(self):
        self._click(self.TYPE_COLOR_VIEW_XPATH)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECTED_TYPE_COLOR_XPATH))).click()

    def choose_type_icon(self):
        self._click(self.TYPE_ICON_IMAGE_XPATH)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SELECTED_TYPE_ICON_XPATH))).click()

    def click_on_ok(self):
        self._click(self.OK_BUTTON_XPATH)

    def check_type(self):
        text_views = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        return any(self.event_type_name.lower() == text_view.text.strip().lower() for text_view in text_views)

    def click_save_changes(self):
        self._click(self.SAVE_CHANGES_BUTTON_XPATH)

    def back_to_home(self):
        self._click(self.HOME_BUTTON_XPATH)

    def add_new_type_flow(self):
        self.find_settings()
        self.find_type_setting()
        self.find_new_type_button()
        self.write_type_name()
        self.choose_type_color()
        self.choose_type_icon()
        self.click_on_ok()
        result = self.check_type()
        self.click_save_changes()
        self.back_to_home()
        return result
