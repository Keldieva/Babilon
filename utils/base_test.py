import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BaseTest(unittest.TestCase):
    def setUp(self, url=None):
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get('http://babilon-m.tj')




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()