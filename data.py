from selenium.webdriver.common.by import By

from helpers import Helpers
from locators.homepage_locators import HomepageLocators
from pages.home_page import Homepage


class Data:
    name = ['Ян', 'Оля', 'Елизавета', 'Иван Иванович']
    surname = ['Иванов', 'Си', 'Бекмамбетов', 'Неразлейводапарочка']
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
    metro_station = ['Бунинская аллея', 'Аэропорт']

    data_form_person_about_1 = [
        ['Ян', 'Иванов', 'Ленинградская, 18', '89999999999', 'Арбатская']
    ]

    data_form_person_about_2 = [
        ['Иван Иванович', 'Неразлейводапарочка', 'Красная Пресня, 1', '+79139137777', 'Бульвар Рокоссовского']
    ]

    data_form_person = [['Ян', 'Иванов', 'Ленинградская, 18', Helpers.phone_1(), 'Павелецкая'],
                        ['Иван Иванович', 'Неразлейводапарочка', 'Красная Пресня, 1', Helpers.phone_2(),
                         'Новохохловская']]

    data_color = ['чёрный жемчуг', 'серая безысходность']

    rent_period = '3'

    date_to_get_scooter = [['январь', '15'], ['март', '27'], ['сентябрь', '1']]

    data_form_about_rent = [['18.03.2025', 5, 'чёрный жемчуг', 'Некогда объяснять, поехали!'],
                            ['02.12.2025', 3, 'серая безысходность', '']]



    question_answer_list = [
        [HomepageLocators.question_list_0, HomepageLocators.answer_text_0],
        [HomepageLocators.question_list_1, HomepageLocators.answer_text_1],
        [HomepageLocators.question_list_2, HomepageLocators.answer_text_2],
        [HomepageLocators.question_list_3, HomepageLocators.answer_text_3],
        [HomepageLocators.question_list_4, HomepageLocators.answer_text_4],
        [HomepageLocators.question_list_5, HomepageLocators.answer_text_5],
        [HomepageLocators.question_list_6, HomepageLocators.answer_text_6],
        [HomepageLocators.question_list_7, HomepageLocators.answer_text_7],
    ]
