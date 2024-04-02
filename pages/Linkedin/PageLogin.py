from selenium.webdriver.common.by import By
from pages import Page
import random

class PageLogin(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    # Page locators definition should go here
    url = "https://www.linkedin.com/"
    txt_email_or_phone = (By.CSS_SELECTOR, "#session_key")
    txt_password = (By.CSS_SELECTOR, "#session_password")

    btn_sign_in = (By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']")
    btn_verify = (By.XPATH, "//button[@id='home_children_button']")
    select_li_for_verify = (By.XPATH, "//div//ul//li[@id='image4']/a")
    iframe_first = (By.XPATH, "//iframe[@id='captcha-internal']")
    iframe_second = (By.XPATH, "//iframe[@id='arkoseframe']")
    iframe_third = (By.XPATH, "//iframe[@data-e2e='enforcement-frame']")
    iframe_four = (By.XPATH, "//iframe[@id='fc-iframe-wrap']")
    iframe_five = (By.XPATH, "//iframe[@id='CaptchaFrame']")

    random_wait_list = [2,3,4,5,6,7,8,9,10,11,12]
    new_number = random.choice(random_wait_list)
    def open(self):
        self.logger.info("first open url")
        self.get("https://www.linkedin.com/")
        self.maximize_window()

    def type_email_or_phone(self):
        self.logger.info("Type email or phone number ")
        self.send_keys(*self.txt_email_or_phone, "mahalsinghchauhan@gmail.com")

    def type_password(self):
        self.wait_for_a_while(self.new_number)
        self.logger.info("Type password")
        self.send_keys(*self.txt_password, "Mahal123@123")

    def click_on_sign_in_button(self):
        self.wait_for_a_while(self.new_number)
        self.logger.info("Click on the sign in button")
        self.click(*self.btn_sign_in)

    def switch_iframe(self):

        self.wait_for_a_while(8)
        # switch first frame
        self.frame("captcha-internal")

        self.logger.info("switch second iframe")

        self.frame("arkoseframe")

        self.logger.info("switch third iframe")
        self.getframe = self.find_element(*self.iframe_third)
        self.frame(self.getframe)

        self.logger.info("switch four iframe")
        self.frame("fc-iframe-wrap")

        self.logger.info("switch five iframe")
        self.frame("CaptchaFrame")

    def click_on_verify_button(self):
        self.logger.info("Click on the verify button")
        self.click(*self.btn_verify)

    def select_verified_(self):
        self.logger.info("Select verify ")
        self.wait_for_a_while(3)
        self.click(*self.select_li_for_verify)



