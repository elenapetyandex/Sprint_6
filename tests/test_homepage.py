import pytest
from selenium import webdriver
from pages.home_page import Homepage
from urls import Urls


class TestHomepage:





    def test_get_answer_for_question_0(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_0()
        assert homepage.check_visibility_answer_0()

    def test_get_answer_for_question_1(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_1()
        assert homepage.check_visibility_answer_1()

    def test_get_answer_for_question_2(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_2()
        assert homepage.check_visibility_answer_2()

    def test_get_answer_for_question_3(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_3()
        assert homepage.check_visibility_answer_3()

    def test_get_answer_for_question_4(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_4()
        assert homepage.check_visibility_answer_4()

    def test_get_answer_for_question_5(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_5()
        assert homepage.check_visibility_answer_5()

    def test_get_answer_for_question_6(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_6()
        assert homepage.check_visibility_answer_6()

    def test_get_answer_for_question_7(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.select_question_from_list_7()
        assert homepage.check_visibility_answer_7()

    def test_upper_order_button(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.allow_cookie()
        homepage.upper_order_button_click()
        homepage.get_current_url()
        assert homepage.get_current_url() == Urls.SCOOTER_ORDER_URL

    def test_lower_order_button(self, driver_1):

        homepage = Homepage(driver_1)

        homepage.scroll_to_lower_order_button()
        homepage.lower_order_button_click()
        assert homepage.get_current_url() == Urls.SCOOTER_ORDER_URL

    def test_yandex_logo_go_to_dzen(self, driver_1):

        homepage = Homepage(driver_1)
        homepage.click_yandex_logo()

        homepage.switch_window()
        homepage.wait_url(Urls.DZEN_URL)
        assert  Urls.DZEN_URL in homepage.get_current_url()





