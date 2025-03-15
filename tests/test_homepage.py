import pytest
from selenium import webdriver

from data import Data
from pages.home_page import Homepage
from urls import Urls
import allure


class TestHomepage:




    @pytest.mark.parametrize('question_locator,answer_text', Data.question_answer_list)
    def test_get_answer_for_question_0(self, driver, question_locator, answer_text):
        driver.get(Urls.SCOOTER_HOMEPAGE_URL)
        homepage = Homepage(driver)
        homepage.allow_cookie()
        homepage.select_question_from_list(question_locator)
        assert homepage.check_visibility_answer(answer_text)



    def test_upper_order_button(self, driver):
        driver.get(Urls.SCOOTER_HOMEPAGE_URL)
        homepage = Homepage(driver)
        homepage.allow_cookie()
        homepage.upper_order_button_click()
        homepage.get_current_url()
        assert homepage.get_current_url() == Urls.SCOOTER_ORDER_URL

    def test_lower_order_button(self, driver):
        driver.get(Urls.SCOOTER_HOMEPAGE_URL)
        homepage = Homepage(driver)

        homepage.scroll_to_lower_order_button()
        homepage.lower_order_button_click()
        assert homepage.get_current_url() == Urls.SCOOTER_ORDER_URL

    def test_yandex_logo_go_to_dzen(self, driver):
        driver.get(Urls.SCOOTER_HOMEPAGE_URL)
        homepage = Homepage(driver)
        homepage.click_yandex_logo()

        homepage.switch_window()
        homepage.wait_url(Urls.DZEN_URL)
        assert  Urls.DZEN_URL in homepage.get_current_url()





