from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))



    def wait_clickable_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)






    def fill_input_field(self, locator, input):
        self.find_element(locator).send_keys(input)

    def clear_field(self, locator):
        self.find_element(locator).clear()


    def get_current_url (self):
        current_url = self.driver.current_url
        return current_url


    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_value(self, locator):
        element = self.find_element(locator)
        return element.get_attribute('value')

    def choose_element_by_count(self, locator, count):
        elements = self.find_elements(locator)
        x = int(count) - 1
        element = elements[x]
        element.click()



    def wait_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(url))

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self, url):
        self.driver.get(url)










