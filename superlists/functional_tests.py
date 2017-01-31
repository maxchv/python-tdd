from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    webdriver_path = 'e:\qa\webdrivers\geckodriver.exe'

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=self.webdriver_path)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a copy new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notice the page title a heard mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test")

        # Sh is invited to enter a to-do item straight away

        # She types 'Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-finishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')
