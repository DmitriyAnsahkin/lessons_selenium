from pages.yandex_page import MainYandexPage
from pygame import mixer


def test_yandex():
    page = MainYandexPage()

    page.driver.get('https://yandex.ru')
    page.click(xpath=page.INPUT_SEARCH)
    page.fill_input(xpath=page.INPUT_SEARCH, value='Привет')
    page.click(xpath=page.BUTTON_SEARCH)

    print()
