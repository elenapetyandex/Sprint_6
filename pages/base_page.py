from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))



    def wait_clickable_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def select_question_from_list(self, locator):
        self.scroll_to_element(locator)
        self.wait_clickable_of_element(locator)
        self.click_on_element(locator)



    def fill_input_field(self, locator, input):
        self.driver.find_element(*locator).send_keys(input)

    def clear_field(self, locator):
        self.driver.find_element(*locator).clear()

    def get_current_url (self):
        current_url = self.driver.current_url
        return current_url


    def find_elements(self, locator):
        self.driver.find_elements(*locator)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def get_value(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute('value')

    def choose_element_by_count(self, locator, count):
        elements = self.driver.find_elements(*locator)
        element = elements[count-1]
        element.click()



    def wait_url(self, Url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(Url))

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])









