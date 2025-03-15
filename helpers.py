import random
import string

from selenium.webdriver.common.by import By



class Helpers:


    @staticmethod
    def get_station_locator_by_station(station):

        xpath = f".//*[text()='{station}']"
        locator = [By.XPATH, xpath]
        return locator

    @staticmethod
    def random_metro_station():
        metro_station_list = [
            'Бульвар Рокоссовского',
            'Сокольники',
            'Бунинская аллея',
            'Новохохловская',
            'Каширская',
            'Красные Ворота',
            'Аэропорт',
            'Павелецкая',
            'Курская',
            'Арбатская',
            'Пушкинская',
            'Зорге'
        ]
        station = random.choice(metro_station_list)


        return station

    @staticmethod
    def phone_1():
        phone_part = ''.join((random.choice(string.digits) for x in range(10)))
        phone_1 = f'+7{phone_part}'
        return phone_1

    @staticmethod
    def phone_2():
        phone_part = ''.join((random.choice(string.digits) for x in range(10)))
        phone_2 = f'8{phone_part}'
        return phone_2

    @staticmethod
    def rent_period_locator(rent_days):
        xpath = f".//div[@class='Dropdown-menu']/div[{rent_days}]]"
        locator = [By.XPATH, xpath]
        return locator

    @staticmethod
    def set_day_locator(day):
        if len(day) == 1:
            xpath = f"div.react-datepicker__day--00{day}"
        elif len(day) == 2:
            xpath = f"div.react-datepicker__day--0{day}"

        locator = [By.CSS_SELECTOR, xpath]
        return locator

    @staticmethod
    def set_data_value(value):
        monthes = {
            '01': 'январь',
            '09': 'сентябрь',
             '03': 'март'
        }
        new_data = []
        value_list = value.split('.')
        day_data = str(int(value_list[0]))
        x = value_list[1]
        month_data = monthes[x]
        new_data.append(day_data)
        new_data.append(month_data)
        new_data.append(value_list[2])
        return new_data


