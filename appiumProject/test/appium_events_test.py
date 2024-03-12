import time
import unittest
from infra.wrapper_page import BasePage
from logic.event_inspector import EventInspector
from logic.event_creator import EventCreator
from logic.event_type_creation import EventTypeCreator


class TestAppiumEvents(unittest.TestCase):
    """Test cases for event features within the app."""

    def setUp(self):
        self.base_case = BasePage()
        self.driver = self.base_case.driver_set_up()
        self.event_name = "Strategy Meeting"
        self.description = "Quarterly strategy meeting with the team"

    def tearDown(self):
        self.driver.quit()

    def test_schedule_conference_call(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)

        # Act
        status = event.add_task_flow()

        # Assert
        self.assertTrue(status)

    def test_set_reminder_for_anniversary(self):
        # Arrange
        event = EventCreator(self.driver, "Anniversary Reminder", "Plan a surprise anniversary party", 3)

        # Act
        status = event.add_task_flow()

        # Assert
        self.assertTrue(status)

    def test_plan_weekly_recap_session(self):
        # Arrange
        event = EventCreator(self.driver, "Weekly Recap", "Summarize the week's achievements and lessons", 2)

        # Act
        status = event.add_task_flow()

        # Assert
        self.assertTrue(status)

    def test_verify_event_in_agenda(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_list = EventInspector(self.driver, self.event_name)

        # Act
        event.add_task_flow()

        # Assert
        self.assertTrue(event_list.verify_flow(), "The strategy meeting should be listed in the agenda.")

    def test_confirm_event_date_on_calendar(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_calendar = EventInspector(self.driver, self.event_name)

        # Act
        day_number = event.add_task_flow()

        # Assert
        self.assertTrue(event_calendar.verify_flow_calendar(day_number),
                        "Meeting date should be marked on the calendar.")

    def test_check_event_visibility_in_weekly_overview(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_week = EventInspector(self.driver, self.event_name)

        # Act
        day_number = event.add_task_flow()

        # Assert
        self.assertTrue(event_week.verify_flow_week(day_number),
                        "The strategy meeting should be visible in the weekly overview.")

    def test_create_custom_event_label(self):
        # Arrange
        new_event_type = EventTypeCreator(self.driver, "Networking")

        # Act
        status = new_event_type.add_new_type_flow()

        # Assert
        self.assertTrue(status, "Failed to create a 'Networking' event label.")

    def test_assign_custom_label_to_new_event(self):
        new_event_type = EventTypeCreator(self.driver, "Networking")
        self.assertTrue(new_event_type.add_new_type_flow(), "Could not add 'Networking' to event labels.")
        event = EventCreator(self.driver, "Industry Mixer", "Connect with industry leaders at the local mixer", 4)
        event.add_task_flow()

    def test_erase_scheduled_meeting(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_deletion = EventInspector(self.driver, self.event_name)

        # Act
        event.add_task_flow()

        # Assert
        self.assertFalse(event_deletion.verify_delete_flow(),
                         "Strategy meeting should have been erased from the schedule.")

    def test_abort_event_cancellation(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_cancel_deletion = EventInspector(self.driver, self.event_name)

        # Act
        event.add_task_flow()

        # Assert
        self.assertTrue(event_cancel_deletion.verify_not_delete_flow(),
                        "Cancellation of meeting deletion should have been aborted.")

    def test_alter_event_details(self):
        # Arrange
        event = EventCreator(self.driver, self.event_name, self.description)
        event_modify = EventInspector(self.driver, self.event_name)

        # Act
        event.add_task_flow()

        # Assert
        self.assertTrue(event_modify.verify_modify_flow(self.event_name),
                        "Details of the meeting should have been altered.")


if __name__ == '__main__':
    unittest.main()
