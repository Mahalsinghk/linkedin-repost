from selenium.webdriver.common.by import By
from pages import Page
import random


class PageHomePage(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    # Page locators definition should go here
    txt_search = (By.CSS_SELECTOR, "input[placeholder='Search']")
    txt_suggestion = (By.XPATH, "//div[@id='triggered-expanded-ember12']")
    select_div = (By.XPATH, "//div[@role='listbox']//div//div")

    random_wait_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    new_number = random.choice(random_wait_list)


    def type_nrobo_search_field(self):
        self.wait_for_a_while(self.new_number)
        self.logger.info("Search Nrobo and press enter")
        self.send_keys(*self.txt_search, "nRoBo Test Automation Framework")
        self.all_elements = self.find_elements(*self.select_div)
        self.all_elements[0].click()
        self.wait_for_a_while(self.new_number)


