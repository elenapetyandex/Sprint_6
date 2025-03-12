from selenium import webdriver
from selenium.webdriver.common.by import By

class HomepageLocators:
    question_list_0 = [By.ID, 'accordion__heading-0']
    question_list_1 = [By.ID, 'accordion__heading-1']
    question_list_2 = [By.ID, 'accordion__heading-2']
    question_list_3 = [By.ID, 'accordion__heading-3']
    question_list_4 = [By.ID, 'accordion__heading-4']
    question_list_5 = [By.ID, 'accordion__heading-5']
    question_list_6 = [By.ID, 'accordion__heading-6']
    question_list_7 = [By.ID, 'accordion__heading-7']
    hidden_question_list = [By.XPATH, ".//div[@hidden='']"]
    allow_cookie_button = [By.ID, 'rcc-confirm-button']
    answer_text_0 = [By.XPATH, ".//p[contains(text(), 'Оплата курьеру')]"]
    answer_text_1 = [By.XPATH, ".//*[contains(text(), 'Пока что у нас так')]"]
    answer_text_2 = [By.XPATH, ".//*[contains(text(), 'Допустим, вы оформляете заказ')]"]
    answer_text_3 = [By.XPATH, ".//*[contains(text(), 'Только начиная с завтрашнего дня')]"]
    answer_text_4 = [By.XPATH, ".//*[contains(text(), 'Пока что нет')]"]
    answer_text_5 = [By.XPATH, ".//*[contains(text(), 'Самокат приезжает к вам с полной зарядкой')]"]
    answer_text_6 = [By.XPATH, ".//*[contains(text(), 'Да, пока самокат не привезли')]"]
    answer_text_7 = [By.XPATH, ".//*[contains(text(), 'Да, обязательно')]"]
    upper_order_button = [By.XPATH, ".//*[@class='Button_Button__ra12g']"]
    lower_order_button = [By.XPATH, ".//button[last()][text()='Заказать']"]
    yandex_logo = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    scooter_logo = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]

