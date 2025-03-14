import allure

from helpers import Helpers
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Дождаться видимости поля "Имя" формы "Для кого самокат"')
    def wait_visible_orderpage(self):
        return self.wait_visibility_of_element(self.locators.name_field)

    @allure.step('Заполнить поле "Имя" формы "Для кого самокат"')
    def fill_input_name(self, name):
        self.fill_input_field(self.locators.name_field, name)

    @allure.step('Заполнить поле "Фамилия" формы "Для кого самокат"')
    def fill_input_surname(self, surname):
        self.fill_input_field(self.locators.surname_field, surname)

    @allure.step('Заполнить поле "Адрес" формы "Для кого самокат"')
    def fill_input_address(self, address):
        self.fill_input_field(self.locators.address_field, address)

    @allure.step('Кликнуть на поле "Станция метро" формы "Для кого самокат" ')
    def click_metro_station(self):
        self.click_on_element(self.locators.select_metro_station_field)



    @allure.step('Заполнить поле "Телефон" формы "Для кого самокат"')
    def fill_input_phone(self, phone):
        self.fill_input_field(self.locators.phone_field, phone)

    @allure.step('Заполнить форму заказа "Для кого самокат" формы "Про аренду" ')
    def fill_form_about_person(self, name, surname,address, phone, station):
        self.fill_input_name(name)
        self.fill_input_surname(surname)
        self.fill_input_address(address)
        self.fill_input_phone(phone)
        self.set_station_by_select(station)

    @allure.step('Кликнуть кнопку "Далее" под формой заказа "Для кого самокат" формы "Про аренду"')
    def click_button_next(self):
        self.click_on_element(self.locators.button_next)

    @allure.step('Дождаться видимости формы заказа "Про аренду"')
    def wait_visible_form_about_rent(self):
        return self.wait_visibility_of_element(self.locators.when_get_scooter)

    @allure.step('Заполнить поле "Когда привезти самокат" введением даты в поле формы "Про аренду"')
    def fill_input_when_get_scooter_by_typing(self, time_get_scooter):
        self.click_on_element(self.locators.when_get_scooter)
        self.fill_input_field(self.locators.when_get_scooter, time_get_scooter)

    @allure.step('Заполнить поле "когда привезти самокат" выбором даты в календаре" формы "Про аренду"')
    def set_month(self, month, day):
        self.click_on_element(self.locators.when_get_scooter)
        while not month in self.get_text(self.locators.current_month):
            self.click_on_element(self.locators.change_month_next)

        self.click_on_element(Helpers.set_day_locator(day))

    @allure.step('Получить значение поля "когда привезти самокат" формы "Про аренду"')
    def get_setted_date(self):
        value = self.get_value(self.locators.when_get_scooter)
        return Helpers.set_data_value(value)



    @allure.step('Получить значение всей формы заказа "Про аренду"')
    def all_form_value(self):
        self.click_on_element(self.locators.all_form)

        return (self.get_text(self.locators.all_form))

    @allure.step('Выбрать срок аренды в поле "срок аренды" формы "Про аренду"')
    def set_rent_period(self, rent_period):
        self.click_on_element(self.locators.all_form) #убрать выпадающий календарь
        self.click_on_element(self.locators.rent_period)
        self.choose_element_by_count(self.locators.rent_period_list, rent_period)

    @allure.step('Выбрать станцию метро из выпадающего списка формы "Для кого самокат"')
    def set_station_by_select(self, station):
        self.click_on_element(self.locators.select_metro_station_field)
        self.click_on_element(Helpers.get_station_locator_by_station(station))
        self.click_on_element(self.locators.all_form)  # чтобы убрать фокус

    @allure.step('Получить значение поля "Станция метро" в форме "Для кого самокат"')
    def check_metro_station_set_up(self):

        return self.get_value(self.locators.select_metro_station_field) #self.get_value(Helpers.get_element_with_of_station(station)) # проверка, что появился элемент с установленным значением станции метро

    @allure.step('Напечатать существующую станцию метро и убедиться, что соответсвующая станция доступна для клика в выпадающем списке')
    def select_metro_station_by_typing(self, station):
        self.click_on_element(self.locators.select_metro_station_field)

        self.fill_input_field(self.locators.select_metro_station_field, station)
        return self.wait_clickable_of_element(Helpers.get_station_locator_by_station(station))

    @allure.step('Выбрать чекбокс в поле "Цвет самоката" формы "Про аренду"')
    def select_scooter_color(self, color):
        if color == 'серая безысходность':
            self.click_on_element(self.locators.scooter_color_checkbox_grey)
        elif color == 'чёрный жемчуг':
            self.click_on_element(self.locators.scooter_color_checkbox_black)

    @allure.step('Кликнуть по кнопке "Заказать" справа под формой "Про аренду"')
    def click_order_button_finally(self):
        self.choose_element_by_count(self.locators.order_buttons, 2)

    @allure.step('Заполнить поле "Комментарий для курьера" формы "Про аренду"')
    def set_comment_for_courier(self, comment):
        self.click_on_element(self.locators.comment_input_field)
        self.fill_input_field(self.locators.comment_input_field, comment)

    @allure.step('Нажать кнопку "Да" в форме "Хотите оформить заказ?"')
    def click_yes_button(self):
        self.click_on_element(self.locators.yes_button)

    @allure.step('Дождаться появления формы "Заказ оформлен"')
    def wait_order_done_pop_up(self):
        return self.wait_visibility_of_element(self.locators.order_done)

    @allure.step('Нажать кнопку "Назад" слева под формой "Про аренду"')
    def click_back_button(self):
        self.click_on_element(self.locators.back_button)
        return self.wait_visibility_of_element(self.locators.name_field)

    @allure.step('Нажать логотип "Самокат"')
    def click_logo_scooter(self):
        self.click_on_element(self.locators.scooter_logo)
























