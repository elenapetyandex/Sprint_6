from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.homepage_locators import HomepageLocators


class Homepage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomepageLocators()

    def allow_cookie(self):
        try:
            self.wait_clickable_of_element(self.locators.allow_cookie_button)
            self.find_element(self.locators.allow_cookie_button)
            self.click_on_element(self.locators.allow_cookie_button)
            self.wait_invisibility_of_element(self.locators.allow_cookie_button)
        except Exception:
            pass





    def select_question_from_list_0(self):
        self.select_question_from_list(self.locators.question_list_0)


    def check_visibility_answer_0(self):
        return self.wait_visibility_of_element(self.locators.answer_text_0)



    def select_question_from_list_1(self):
        self.select_question_from_list(self.locators.question_list_1)

    def check_visibility_answer_1(self):
        return self.wait_visibility_of_element(self.locators.answer_text_1)



    def select_question_from_list_2(self):
        self.select_question_from_list(self.locators.question_list_2)

    def check_visibility_answer_2(self):
        return self.wait_visibility_of_element(self.locators.answer_text_2)


    def select_question_from_list_3(self):
        self.select_question_from_list(self.locators.question_list_3)

    def check_visibility_answer_3(self):

        return self.wait_visibility_of_element(self.locators.answer_text_3)

    def select_question_from_list_4(self):
        self.select_question_from_list(self.locators.question_list_4)

    def check_visibility_answer_4(self):
        return self.wait_visibility_of_element(self.locators.answer_text_4)

    def select_question_from_list_5(self):
        self.select_question_from_list(self.locators.question_list_5)

    def check_visibility_answer_5(self):
        return self.wait_visibility_of_element(self.locators.answer_text_5)

    def select_question_from_list_6(self):
        self.select_question_from_list(self.locators.question_list_6)

    def check_visibility_answer_6(self):
        return self.wait_visibility_of_element(self.locators.answer_text_6)

    def select_question_from_list_7(self):
        self.select_question_from_list(self.locators.question_list_7)

    def check_visibility_answer_7(self):
        return self.wait_visibility_of_element(self.locators.answer_text_7)

    def upper_order_button_click(self):
        self.click_on_element(self.locators.upper_order_button)

    def lower_order_button_click(self):
        self.click_on_element(self.locators.lower_order_button)

    def scroll_to_lower_order_button(self):
        self.scroll_to_element(self.locators.lower_order_button)



    def click_yandex_logo(self):
        self.click_on_element(self.locators.yandex_logo)



