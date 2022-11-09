from utils.base_test import BaseTest

class Base_Page(BaseTest):
    def test_title_tc001(self):
    # assertion to confirm if title has keyword in it
        self.assertIn("Главная", self.driver.title)