from typing import Optional

from nrobo.selenese import AnyBy
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
    from nrobo.util.common import Common
    random_number = Common.generate_random_numbers(1,8)
    btn_repost = (By.XPATH, "//span[text()='Repost']/..")
    btn_share_all = (By.XPATH, "//span[text()='Share']//parent::button")
    btn_repost_with_your_throught = (By.XPATH, "//span[text()='Repost with your thoughts']/..")
    p_tag_insert_description = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")
    btn_post = (By.XPATH, "//span[text()='Post']//parent::button")
    drp_profile_name = (By.CSS_SELECTOR, ".share-unified-settings-entry-button")
    chk_group_for_post = (By.CSS_SELECTOR, "#CONTAINER")
    chk_select_group_for_post = (By.XPATH, "//div[@class='sharing-shared-generic-list__item']//button")
    rdo_select_groups = (By.XPATH, "//button[@class='sharing-shared-generic-list__item-button']//span[@class='sharing-shared-generic-list__description-single-line']")
    btn_save_group = (By.XPATH, "//span[text()='Save']//parent::button")
    btn_done_group = (By.XPATH, "//span[text()='Done']//parent::button")
    btn_save_disabled = (By.XPATH, "//span[text()='Save']//parent::button[@disabled]")
    btn_nrobo__skip = (By.XPATH, "//div[@class='sharing-shared-generic-list__item']//button[@aria-checked='true']")
    btn_back = (By.XPATH, "//span[text()='Back']//parent::button")
    btn_cross_icon = (By.XPATH, "//button[@class='artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view artdeco-modal__dismiss']")
    btn_discard = (By.XPATH, "//span[text()='Discard']//parent::button")


    def click_on_share_button(self):
        self.logger.info("Click on the share button")
        self.wait_for_a_while(self.random_number)
        self.all_element_of_share = self.find_elements(*self.btn_share_all)
        self.all_element_of_share[1].click()


    def click_on_repost_button(self):
        self.wait_for_a_while(self.random_number)
        self.logger.info("Click on the repost button")
        self.click(*self.btn_repost)

    def click_on_repost_with_your_throught(self):
        self.wait_for_a_while(self.random_number)
        self.logger.info("Click on the Repost with your throught")
        self.click(*self.btn_repost_with_your_throught)

    def type_description_for_repost(self):
        self.logger.info("Type description for repost")
        with open('nrobo-linkedin.yaml', 'r') as file:
            prime_service = yaml.safe_load(file)
        self.wait_for_a_while(self.random_number)
        new_through = "Hello Panchdev, #{}\nYoutube video tutorial:{}\n{}".format(prime_service["my_key"]["key1"], prime_service["my_key"]["key2"], prime_service["my_key"]["key3"])
        self.send_keys(*self.p_tag_insert_description, new_through)

    def click_on_post_button(self):
        self.logger.info("Click on the post button")
        self.wait_for_a_while(self.random_number)
        self.click(*self.btn_post)
        self.wait_for_a_while(self.random_number)

    def click_on_the_view_profile_for_group(self):
        self.logger.info("Click on the view profile icon for select group")
        self.wait_for_a_while(self.random_number)
        self.click(*self.drp_profile_name)

    def select_group_in_post_setting_popup(self):
        self.logger.info("select group checkbox in the group popup setting")
        self.wait_for_a_while(self.random_number)
        self.click(*self.chk_group_for_post)

    # def select_group_one_by_one_in_select_group_popup(self):
    #     self.logger.info("Select group one by one in the select group popup")
    #     self.wait_for_a_while(self.random_number)
    #     self.select_all_group = self.find_elements(*self.rdo_select_groups)
    #
    #     for x in range(len(self.select_all_group)):
    #         self.groups = self.find_elements(*self.rdo_select_groups)
    #         group_name = self.select_all_group[x].text
    #         self.logger.info(f"this is text:{group_name}")
    #         self.select_all_group[x].click()
    #         if group_name == "nRoBo Test Automation Framework":
    #             self.logger.info("nrobo is match")
    #             continue
    #
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info(f"click on the save button{x}")
    #         self.click(*self.btn_save_group)
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("click on the done button")
    #         self.click(*self.btn_done_group)
    #         self.logger.info("click on the Post button")
    #         self.wait_for_a_while(self.random_number)
    #         self.click_on_post_button()
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("Again click on the share button")
    #         self.click_on_repost_button()
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("Again click on the repost throught")
    #         self.click_on_repost_with_your_throught()
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("Again enter description")
    #         self.type_description_for_repost()
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("Again click on the repost throught")
    #         self.click_on_the_view_profile_for_group()
    #         self.wait_for_a_while(self.random_number)
    #         self.logger.info("Again click on the repost throught")
    #         self.select_group_in_post_setting_popup()
    #         self.wait_for_a_while(self.random_number)

    def select_groups_and_repost(self):
        self.logger.info("Select group one by one in the select group popup")
        self.wait_for_a_while(self.random_number)
        groups = self.find_elements(*self.rdo_select_groups)
        self.click(*self.btn_back)
        self.logger.info("go to the back")
        self.wait_for_a_while(self.random_number)
        self.click(*self.btn_back)
        self.wait_for_a_while(self.random_number)
        self.click(*self.btn_cross_icon)
        self.wait_for_a_while(self.random_number)
        self.click(*self.btn_discard)
        for index in range(len(groups)):
            self.wait_for_a_while(self.random_number)
            self.click_on_repost_button()
            self.click_on_repost_with_your_throught()
            self.type_description_for_repost()
            self.wait_for_a_while(self.random_number)
            self.click_on_the_view_profile_for_group()
            self.wait_for_a_while(self.random_number)
            self.select_group_in_post_setting_popup()

            groups = self.find_elements(*self.rdo_select_groups)
            groups[index].click()
            groups_name = groups[index].text
            if groups_name == "nRoBo Test Automation Framework":
                self.wait_for_a_while(self.random_number)
                self.click(*self.btn_back)
                self.wait_for_a_while(self.random_number)
                self.click(*self.btn_cross_icon)
                self.wait_for_a_while(self.random_number)
                self.click(*self.btn_discard)
                continue

            self.wait_for_a_while(self.random_number)
            self.click(*self.btn_back)
            self.wait_for_a_while(self.random_number)
            self.click(*self.btn_cross_icon)
            self.wait_for_a_while(self.random_number)
            self.click(*self.btn_discard)
            # self.click(*self.btn_save_group)
            # self.wait_for_a_while(self.random_number)
            # self.click(*self.btn_done_group)
            # self.wait_for_a_while(self.random_number)
            # self.click(*self.btn_post)
            # self.click_on_repost_button()
            # self.click_on_repost_with_your_throught()
            # self.type_description_for_repost()











