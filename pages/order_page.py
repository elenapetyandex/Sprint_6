from helpers import Helpers
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()



    def wait_visible_orderpage(self):
        return self.wait_visibility_of_element(self.locators.name_field)

    def fill_input_name(self, name):
        self.fill_input_field(self.locators.name_field, name)

    def fill_input_surname(self, surname):
        self.fill_input_field(self.locators.surname_field, surname)

    def fill_input_address(self, address):
        self.fill_input_field(self.locators.address_field, address)

    def click_metro_station(self):
        self.click_on_element(self.locators.select_metro_station_field)

    def select_metro_station_from_list(self):

        self.click_on_element(self.locators.metro_station_to_choice)




    def fill_input_phone(self, phone):

        self.fill_input_field(self.locators.phone_field, phone)

    def fill_form_about_person(self, name, surname,address, phone, station):
        self.fill_input_name(name)
        self.fill_input_surname(surname)
        self.fill_input_address(address)
        self.fill_input_phone(phone)
        self.set_station_by_select(station)

    def click_button_next(self):
        self.click_on_element(self.locators.button_next)

    def wait_visible_form_about_rent(self):
        return self.wait_visibility_of_element(self.locators.when_get_scooter)


    def fill_input_when_get_scooter_by_typing(self, time_get_scooter):
        self.click_on_element(self.locators.when_get_scooter)
        self.fill_input_field(self.locators.when_get_scooter, time_get_scooter)

    def fill_input_when_get_scooter_by_select(self, month):
        self.click_on_element(self.locators.when_get_scooter)
        self.click_on_element(self.locators.change_month_next)
        text_element = self.find_element(self.locators.current_month).text
        while not month in text_element:
            self.click_on_element(self.locators.change_month_next)



    def set_month(self, month, day):
        self.click_on_element(self.locators.when_get_scooter)
        while not month in self.get_text(self.locators.current_month):
            self.click_on_element(self.locators.change_month_next)

        self.click_on_element(Helpers.set_day_locator(day))


    def get_setted_date(self):
        value = self.get_value(self.locators.when_get_scooter)
        return Helpers.set_data_value(value)



    def choose_rent_period(self, day_count):
        self.click_on_element(self.locators.rent_period)

        self.find_element(self.locators.rent_period_pop_up)

        self.scroll_to_element(self.locators.rent_one_day)

        self.click_on_element(self.locators.rent_one_day)




    def all_form_value(self):
        self.click_on_element(self.locators.all_form)

        return (self.get_text(self.locators.all_form))

    def set_rent_period(self, rent_period):
        self.click_on_element(self.locators.all_form) #убрать выпадающий календарь
        self.click_on_element(self.locators.rent_period)
        self.choose_element_by_count(self.locators.rent_period_list, rent_period)

    def set_station_by_select(self, station):
        self.click_on_element(self.locators.select_metro_station_field)
        self.click_on_element(Helpers.get_station_locator_by_station(station))
        self.click_on_element(self.locators.all_form)  # чтобы убрать фокус

    def check_metro_station_set_up(self):

        print(self.get_value(self.locators.select_metro_station_field))
        return self.get_value(self.locators.select_metro_station_field) #self.get_value(Helpers.get_element_with_of_station(station)) # проверка, что появился элемент с установленным значением станции метро


    def select_metro_station_by_typing(self, station):
        self.click_on_element(self.locators.select_metro_station_field)

        self.fill_input_field(self.locators.select_metro_station_field, station)
        return self.wait_clickable_of_element(Helpers.get_station_locator_by_station(station))



    def select_scooter_color(self, color):
        if color == 'серая безысходность':
            self.click_on_element(self.locators.scooter_color_checkbox_grey)
        elif color == 'чёрный жемчуг':
            self.click_on_element(self.locators.scooter_color_checkbox_black)

    def click_order_button_finally(self):
        self.choose_element_by_count(self.locators.order_buttons, 2)

    def set_comment_for_courier(self, comment):
        self.click_on_element(self.locators.comment_input_field)
        self.fill_input_field(self.locators.comment_input_field, comment)

    def click_yes_button(self):
        self.click_on_element(self.locators.yes_button)

    def wait_order_done_pop_up(self):
        return self.wait_visibility_of_element(self.locators.order_done)

    def click_back_button(self):
        self.click_on_element(self.locators.back_button)
        return self.wait_visibility_of_element(self.locators.name_field)

    def click_logo_scooter(self):
        self.click_on_element(self.locators.scooter_logo)
























