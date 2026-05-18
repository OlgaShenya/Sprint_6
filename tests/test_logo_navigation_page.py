import pytest
import allure
from locators.main_locators import MainLocators


@pytest.mark.usefixtures("driver", "main_page")
class TestLogoNavigation:

    @allure.title('Проверка редиректа по клику на логотип')
    @allure.description('Проверяет переход по логотипам Самоката и Яндекса')
    @pytest.mark.parametrize("locator, expected_elements, opens_new_tab", [
        pytest.param(
            MainLocators.LOGO_SAMOKAT,
            [MainLocators.SAMOKAT_PAGE_ELEMENT],
            False,
            id="samokat_same_tab"
        ),
        pytest.param(
            MainLocators.LOGO_YANDEX,
            [MainLocators.YANDEX_PAGE_ELEMENT, MainLocators.YANDEX_PAGE_ALTERNATIVE_ELEMENT],
            True,
            id="yandex_new_tab_with_fallback"
        ),
    ])
    def test_logo_redirects(self, driver, main_page, locator, expected_elements, opens_new_tab):
        main_page.accept_cookies_if_present()
        initial_count = len(driver.window_handles)
        main_page.click_element(locator)
        main_page.switch_tab_if_needed(opens_new_tab, initial_count)
        element = main_page.find_first_displayed_element(expected_elements, timeout=10)
        assert element is not None and element.is_displayed(), (
            f"Не найден ни один из ожидаемых элементов: {expected_elements}. "
            f"Либо элемент отсутствует в DOM, либо не отображается на странице."
        )
