from typing import Optional

from nrobo.selenese import AnyBy
from selenium.webdriver.common.by import By
from pages import Page
import yaml
import random

class PageGroup(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    random_wait_list = [2, 3, 4, 5, 6]
    new_number = random.choice(random_wait_list)

    btn_repost = (By.XPATH, "//span[text()='Repost']/..")
    btn_repost_with_your_throught = (By.XPATH, "//span[text()='Repost with your thoughts']/..")
    p_tag_insert_description = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")
    btn_post = (By.XPATH, "//span[text()='Post']//..")
    drp_profile_name = (By.CSS_SELECTOR, ".share-unified-settings-entry-button")
    chk_group_for_post = (By.CSS_SELECTOR, "#CONTAINER")
    chk_select_group_for_post = (By.XPATH, "//div[@class='sharing-shared-generic-list__item']//button")
    btn_save_group = (By.XPATH, "//span[text()='Save']//parent::button")
    btn_done_group = (By.XPATH, "//span[text()='Done']//parent::button")
    btn_save_disabled = (By.XPATH, "//span[text()='Save']//parent::button[@disabled]")


    def click_on_repost_button(self):
        self.wait_for_a_while(self.new_number)
        self.logger.info("Click on the repost button")
        self.click(*self.btn_repost)

    def click_on_repost_with_your_throught(self):
        self.wait_for_a_while(self.new_number)
        self.logger.info("Click on the Repost with your throught")
        self.click(*self.btn_repost_with_your_throught)

    def type_description_for_repost(self):
        self.logger.info("Type description for repost")
        with open('nrobo-linkedin.yaml', 'r') as file:
            prime_service = yaml.safe_load(file)
        self.wait_for_a_while(self.new_number)
        new_through = "Hello Panchdev, #{}\nYoutube video tutorial:{}\n{}".format(prime_service["my_key"]["key1"], prime_service["my_key"]["key2"], prime_service["my_key"]["key3"])
        self.send_keys(*self.p_tag_insert_description, new_through)

    def click_on_post_button(self):
        self.logger.info("Click on the post button")
        self.wait_for_a_while(self.new_number)
        self.click(*self.btn_post)
        self.wait_for_a_while(self.new_number)

    def click_on_the_view_profile_for_group(self):
        self.logger.info("Click on the view profile icon for select group")
        self.wait_for_a_while(self.new_number)
        self.click(*self.drp_profile_name)

    def select_group_in_post_setting_popup(self):
        self.logger.info("select group checkbox in the group popup setting")
        self.wait_for_a_while(self.new_number)
        self.click(*self.chk_group_for_post)

    def select_group_one_by_one_in_select_group_popup(self):
        self.logger.info("Select group one by one in the select group popup")
        self.wait_for_a_while(self.new_number)

        self.select_all_group = self.find_elements(*self.chk_select_group_for_post)

        for x in range(len(self.select_all_group)):
            #x = x+1
            self.select_all_group = self.find_elements(*self.chk_select_group_for_post)
            self.select_all_group[x].click()
            self.wait_for_a_while(self.new_number)
            self.click(*self.btn_save_group)
            self.wait_for_a_while(self.new_number)
            self.click(*self.btn_done_group)
            self.click_on_the_view_profile_for_group()
            self.select_group_in_post_setting_popup()
            self.wait_for_a_while(self.new_number)

