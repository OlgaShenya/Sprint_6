import pytest
import allure
from locators.order_locators import OrderLocators


@pytest.mark.usefixtures("order_page")
class TestOrderPage:

    @allure.title('Позитивный сценарий заказа самоката')
    @allure.description('Проверка полного флоу заказа через две точки входа с двумя наборами данных')
    @pytest.mark.parametrize(
        "order_button, name, surname, address, metro, phone, date, duration, color, comment",
        [
            (OrderLocators.ORDER_BTN_TOP,
             "Иван", "Иванов", "ул. Пушкина, д.1", "Черкизовская", "89991234567",
             "01.01.2027", "сутки", "чёрный", "Позвоните за час"),
            (OrderLocators.ORDER_BTN_BOTTOM,
             "Мария", "Петрова", "ул. Ленина, д.5", "Сокольники", "89997654321",
             "02.01.2027", "двое суток", "серый", None),
        ],
        ids=["top_button", "bottom_button"]
    )
    def test_order_success(self, order_page, order_button, name, surname,
                           address, metro, phone, date, duration, color, comment):
        order_page.click_element(order_button)
        order_page.fill_personal_info(name, surname, address, metro, phone)
        order_page.click_next()
        order_page.fill_rent_info(date, duration, color, comment)
        order_page.click_order()
        order_page.confirm_order()
        modal = order_page.find_element(OrderLocators.ORDER_MODAL)
        assert modal is not None and modal.is_displayed(), "Модальное окно 'Заказ оформлен' не появилось"

