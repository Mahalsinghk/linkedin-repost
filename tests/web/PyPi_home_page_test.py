"""
@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import pytest
from pages.PagePyPiHome import PagePyPiHome
from pages.Linkedin.PageLogin import PageLogin
from pages.Linkedin.PageHomePage import PageHomePage
from pages.Linkedin.PageSearch import PageSearch
from pages.Linkedin.PageGroup import PageGroup


class TestPyPiHomePage():

    @pytest.mark.unit
    @pytest.mark.skip(reason="Test is not yet complete")
    def test_must_a_failure(self, driver, logger):
        logger.info("This test will fail for sure")
        driver.get("https://google.com")
        raise Exception("Must a fail test")

    @pytest.mark.unit
    def test_this_will_pass_always(self, driver, logger):
        logger.info("this test will pass always")
        driver.get("https://google.com")

    @pytest.mark.unit
    @pytest.mark.skip
    def test_pass_app_name_from_commandline(self, logger, app):
        logger.info(f"Appname={app}")

    @pytest.mark.unit
    @pytest.mark.skip
    def test_pass_url_username_password_from_commandline_example(self, driver, logger, url, username, password):
        logger.info(f"URL={url}, Username={username} and Password={password}")
        driver.get(url)

    @pytest.mark.sanity
    def test_google_branding_displayed_on_home_page(self, driver, logger):
        # Instantiate page object
        page_pypi_home = PagePyPiHome(driver, logger)
        # call page method
        page_pypi_home.open()

        # Asset test condition
        assert page_pypi_home.search_button_present() == True

    @pytest.mark.regression
    def test_nrobo_package_is_available_on_pypi_org(self, driver, logger):
        page_pypi_home = PagePyPiHome(driver, logger)

        page_pypi_home.open()

        page_pypi_home.type_search_keyword("nrobo")

        page_search = page_pypi_home.search()

        # put a checkpoint
        assert page_search.nrobo_link_is_present()

    @pytest.mark.xfail
    @pytest.mark.skip(reason="Wanted to skip it for easy demonstration")
    def test_this_will_fail_for_sure(self, driver, logger):
        raise Exception("Must fail")

    @pytest.mark.sanity
    def test_search_nrobo_and_repost_latest_post(self, driver, logger):
        page_login = PageLogin(driver, logger)
        page_login.open()
        page_login.type_email_or_phone()
        page_login.type_password()
        page_login.click_on_sign_in_button()

        #this object for linkedin homepage
        page_home_page = PageHomePage(driver, logger)
        page_home_page.type_nrobo_search_field()

        #this object for search page
        page_search = PageSearch(driver, logger)
        page_search.click_nrobo_test_automation_framework()

        #this object for paggroup
        page_group = PageGroup(driver, logger)
        page_group.click_on_repost_button()
        page_group.click_on_repost_with_your_throught()
        page_group.type_description_for_repost()
        # page_group.click_on_post_button()
        page_group.click_on_the_view_profile_for_group()
        page_group.select_group_in_post_setting_popup()
        page_group.select_group_one_by_one_in_select_group_popup()

