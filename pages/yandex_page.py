from pages.base_page import BasePage


class MainYandexPage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys('Я все равно сюда затолкаю то что хочу')
