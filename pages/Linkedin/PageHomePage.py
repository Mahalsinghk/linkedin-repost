from selenium.webdriver.common.by import By
from pages import Page


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



    def type_nrobo_search_field(self):
        self.logger.info("Search Nrobo and press enter")
        self.send_keys(*self.txt_search, "nrobo")
        self.click(*self.select_div)
        self.wait_for_a_while(3)



