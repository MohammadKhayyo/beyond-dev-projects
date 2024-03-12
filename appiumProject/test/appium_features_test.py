import unittest
from infra.wrapper_page import BasePage
from logic.check_arrows import CheckArrows
from logic.theme_color_changer import ThemeColorChanger
from logic.vibrate_setting_manager import VibrateSettingManager


class TestAppiumFeatures(unittest.TestCase):

    def setUp(self):
        self.base_case = BasePage()
        self.driver = self.base_case.driver_set_up()
        self.themes = ThemeColorChanger(self.driver)
        self.arrows = CheckArrows(self.driver)
        self.vibes = VibrateSettingManager(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_change_theme_color(self):
        status = self.themes.update_theme_color()
        self.assertTrue(status)

    def test_arrows_right_moves(self):
        difference = self.arrows.arrows_flow("next")
        self.assertEqual(difference, 7, f"The date difference is {difference}, expected 7")

    def test_arrows_left_moves(self):
        difference = self.arrows.arrows_flow("prev")
        self.assertEqual(difference, 7, f"The date difference is {difference}, expected 7")

    def test_vibrate_change(self):
        initial_state, new_state = self.vibes.modify_vibration_setting()
        self.assertNotEqual(initial_state, new_state, "Vibrate state should have changed but did not")


if __name__ == '__main__':
    unittest.main()
