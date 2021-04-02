from selenium import webdriver
import unittest

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/app_exorcist/Code/flask-ner/test/geckodriver")
        # link to the web ui
        self.driver.get("localhost:3000")


    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)
    
    def test_page_has_input_for_text(self):
        input_element = self._find("input-text")
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find("find-button")
        self.assertIsNotNone(submit_button)
    
    # TODO: Write a test to make sure that textarea is shown on the page
    # TODO: Write a test to make sure that after submitting input, textarea gets  filled
    # with respone data

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"')