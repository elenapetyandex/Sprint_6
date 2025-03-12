
from urls import Urls
from pages.order_page import OrderPage

import pytest
from data import Data



class TestOrderPage():

    def tests_select_station_set_value_in_field(self, driver,station='Пушкинская'):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.set_station_by_select(station)
        assert orderpage.check_metro_station_set_up() == station

    def tests_input_station_by_typing_calls_station_to_select(self, driver,station='Пушкинская'):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        assert orderpage.select_metro_station_by_typing(station)

    @pytest.mark.parametrize('name,surname,address, phone, station', Data.data_form_person)
    def test_filled_form_person_about(self, driver,  name, surname,address, phone, station):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person( name, surname, address, phone, station)
        orderpage.click_button_next()
        assert orderpage.wait_visible_form_about_rent()

    @pytest.mark.parametrize('name,surname,address, phone, station', Data.data_form_person_about_1)
    def test_click_back_button_on_about_rent_form_go_to_person_about_form(self, driver, name, surname, address, phone, station):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person(name, surname, address, phone, station)
        orderpage.click_button_next()
        assert orderpage.click_back_button()

    @pytest.mark.parametrize('name,surname,address, phone, station', Data.data_form_person_about_2)
    @pytest.mark.parametrize('month,day', Data.date_to_get_scooter)
    def test_fill_input_when_get_scooter_by_select(self, driver, name, surname, address, phone, station, month, day):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person(name, surname, address, phone, station)
        orderpage.click_button_next()
        orderpage.set_month(month, day)
        assert day in orderpage.get_setted_date() and month in orderpage.get_setted_date()

    def test_fill_input_when_get_scooter_by_typing(self,driver, time_get_scooter):
        orderpage = OrderPage(driver)





    def test_choose_rent_period(self, driver, rent_period=3):

        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person('анастасия', 'ивановна', 'Маяковского', '89999999999', 'Пушкинская')
        orderpage.click_button_next()
        orderpage.set_rent_period(rent_period)
        assert 'трое суток' in  orderpage.all_form_value()



    @pytest.mark.parametrize('color', Data.data_color)
    def test_chekbox_choose_color(self, driver, color):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person('анастасия', 'ивановна', 'Маяковского', '89999999999', 'Пушкинская')
        orderpage.click_metro_station()
        orderpage.select_metro_station_from_list()
        orderpage.click_button_next()
        orderpage.select_scooter_color(color)
        assert color in  orderpage.all_form_value()

    @pytest.mark.parametrize('date, rent_period, color,comment', Data.data_form_about_rent)
    def test_get_order(self, driver,date, rent_period, color, comment):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.fill_form_about_person('анастасия', 'ивапн', 'лаоарппа', '89999999999', 'Пушкинская')
        orderpage.click_button_next()
        orderpage.fill_input_when_get_scooter_by_typing(date)
        orderpage.set_rent_period(rent_period)
        orderpage.select_scooter_color(color)
        orderpage.set_comment_for_courier(comment)
        orderpage.click_order_button_finally()
        orderpage.click_yes_button()
        assert orderpage.wait_order_done_pop_up()

    def test_click_scooter_logo_go_to_homepage(self, driver):
        orderpage = OrderPage(driver)
        orderpage.wait_visible_orderpage()
        orderpage.click_logo_scooter()
        orderpage.wait_url(Urls.SCOOTER_HOMEPAGE_URL)
        assert orderpage.get_current_url() == Urls.SCOOTER_HOMEPAGE_URL












