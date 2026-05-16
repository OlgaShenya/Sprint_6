import pytest
import allure
from locators.main_locators import MainLocators
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("driver", "main_page")
class TestLogoNavigation:
    @allure.title('Проверка редиректа по клику на логотип')
    @allure.description('Проверяет переход по логотипам Самоката и Яндекса')
    @pytest.mark.parametrize("locator, expected_element, opens_new_tab", [
        (MainLocators.LOGO_SAMOKAT, MainLocators.SAMOKAT_PAGE_ELEMENT, False),
        (MainLocators.LOGO_YANDEX, MainLocators.YANDEX_PAGE_ELEMENT, True),
    ])
    def test_logo_redirects(self, driver, main_page, locator, expected_element, opens_new_tab):
        main_page.accept_cookies_if_present()
        initial_count = len(driver.window_handles)
        main_page.click_element(locator)

        if opens_new_tab:
            main_page.wait_for_new_window_and_load(initial_count=initial_count)
        try:
            main_page.wait_for_element_located(expected_element, timeout=10)
            element = driver.find_element(*expected_element)
            assert element.is_displayed(), "Ожидаемый элемент страницы не отображается"
            
        except TimeoutException:
            main_page.wait_for_element_located(MainLocators.YANDEX_PAGE_ALTERNATIVE_ELEMENT, timeout=5)
            alt_element = driver.find_element(*MainLocators.YANDEX_PAGE_ALTERNATIVE_ELEMENT)
            assert alt_element.is_displayed(), \
                "Не найден ни основной элемент, ни альтернативный (капча?)"
