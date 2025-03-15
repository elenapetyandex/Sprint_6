from selenium.webdriver.common.by import By

from helpers import Helpers


class OrderPageLocators:
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]  #
    surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]  #
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]  #
    select_metro_station_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  #
    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  #
    button_next = [By.XPATH, ".//button[text()='Далее']"]  #
    metro_station_to_choice = [By.XPATH, ".//*[text()='Пушкинская']"]  # Выбор станции в поле "Станция метро"
    when_get_scooter = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  #
    rent_period = [By.XPATH, ".//div[text()='* Срок аренды']"]  #
    scooter_color = [By.XPATH, ".//div[text()='Цвет самоката']"]  #
    scooter_color_checkbox_black = [By.ID, 'black']  #
    scooter_color_checkbox_grey = [By.ID, 'grey']  #
    comment_input_field = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]  #
    order_buttons = [By.XPATH, ".//button[text()='Заказать']"]  # две кнопки "Заказать" в форме "Про аренду"

    data_pop_form = [By.XPATH, ".//*[@class='react-datepicker-popper']"]  #
    change_month_next = [By.XPATH, ".//button[text()='Next Month']"]  #
    change_month_previous = [By.XPATH, ".//button[text()='Previous Month']"]  #
    chosen_day = [By.CLASS_NAME, 'react-datepicker__day--selected']  #
    current_month = [By.XPATH, ".//div[@class='react-datepicker__current-month']"]  #месяц в календаре
    day_to_choose_from_calendar = [By.CSS_SELECTOR, "div.react-datepicker__day--008" ]  #
    rent_period_list = [By.XPATH, ".//div[@class='Dropdown-menu']/div"]  # выпадающий список сроков аренды
    rent_period_pop_up = [By.XPATH, ".//div[@class='Dropdown-menu']"]  #
    rent_period_chosen = [By.CSS_SELECTOR, "[@aria-selected='true']"]  #
    rent_one_day = [By.XPATH, ".//div[@class='Dropdown-menu']/div[1]"]  #
    rent_field_filled = [By.CSS_SELECTOR, "div.Dropdown-placeholder.is-selected"]  #
    rent_assert = [By.XPATH, ".//*[text()='сутки']"]  #
    all_form = [By.XPATH, ".//div[@class='Order_Content__bmtHS']"]  # формы для заполнения "Для кого самокат" и "про аренду"
    yes_button = [By.XPATH, ".//button[text()='Да']"]  #
    order_done = [By.XPATH, ".//*[text()='Заказ оформлен']"]  #
    back_button = [By.XPATH, ".//*[text()='Назад']"] #
    scooter_logo = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]
    random_station_locator = Helpers.get_station_locator_by_station(Helpers.random_metro_station)