from selenium.webdriver.common.by import By
from pages import Page
import yaml

class PageGroup(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this
    btn_repost = (By.XPATH, "//span[text()='Repost']/..")
    btn_repost_with_your_throught = (By.XPATH, "//span[text()='Repost with your thoughts']/..")
    p_tag_insert_description = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")



    def click_on_repost_button(self):
        self.logger.info("Click on the repost button")
        self.click(*self.btn_repost)

    def click_on_repost_with_your_throught(self):
        self.logger.info("Click on the Repost with your throught")
        self.click(*self.btn_repost_with_your_throught)

    def type_description_for_repost(self):
        self.logger.info("Type description for repost")
        with open('nrobo-linkedin.yaml', 'r') as file:
            prime_service = yaml.safe_load(file)

        self.send_keys(*self.p_tag_insert_description, prime_service['mydescription'])

        self.wait_for_a_while(5)