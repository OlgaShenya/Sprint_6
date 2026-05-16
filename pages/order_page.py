import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):

    @allure.step('Заполнить личные данные: {name} {surname}')
    def fill_personal_info(self, name, surname, address, metro, phone):
        self.fill_input(OrderLocators.NAME, name)
        self.fill_input(OrderLocators.SURNAME, surname)
        self.fill_input(OrderLocators.ADDRESS, address)
        self.select_metro_station(metro)
        self.fill_input(OrderLocators.PHONE, phone)

    @allure.step('Выбрать станцию метро: {station_name}')
    def select_metro_station(self, station_name):
        self.click_element(OrderLocators.STATION_INPUT)
        locator = OrderLocators.get_station_option(station_name)
        self.click_element(locator)

    @allure.step('Нажать "Далее"')
    def click_next(self):
        self.click_element(OrderLocators.NEXT_BTN)

    @allure.step('Заполнить детали аренды: {date}, {duration}')
    def fill_rent_info(self, date, duration, color=None, comment=None):
        self.fill_date(date)
        self.select_duration(duration)
        if color:
            self.select_color(color)
        if comment:
            self.fill_input(OrderLocators.COMMENT, comment)

    def fill_date(self, date):
        element = self.driver.find_element(*OrderLocators.DELIVERY_DATE)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def select_duration(self, duration_text):
        self.click_element(OrderLocators.DURATION_DROPDOWN)
        locator = OrderLocators.get_duration_option(duration_text)
        self.click_element(locator)

    def select_color(self, color):
        color_locators = {
            'чёрный': OrderLocators.COLOR_BLACK,
            'серый': OrderLocators.COLOR_GREY,
        }
        self.click_element(color_locators[color])

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        self.click_element(OrderLocators.ORDER_BTN)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderLocators.CONFIRMATION_BTN)

    @allure.step('Нажать "Посмотреть статус"')
    def click_view_status(self):
        self.click_element(OrderLocators.STATUS_BTN)
