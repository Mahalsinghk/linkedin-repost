from selenium.webdriver.common.by import By
from pages import Page
import random

class PageSearch(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    random_number = random.randint(1,6)

    lnk_nrobo_framework_text = (By.XPATH, "//a[text()='nRoBo Test Automation Framework']")
    def click_nrobo_test_automation_framework(self):
        self.wait_for_a_while(self.random_number)
        self.logger.info("Click on the nrobo test automation framework link")
        self.click(*self.lnk_nrobo_framework_text)




