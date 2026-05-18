from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, element, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))

    def wait_for_element_clickable(self, element, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))

    def wait_for_element_located(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_to_center(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
            element
        )

    def refresh_page(self):
        self.driver.refresh()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Принять куки, если баннер отображается")
    def accept_cookies_if_present(self):
        from locators.main_locators import MainLocators
        try:
            self.click_element(MainLocators.COOKIE_ACCEPT_BTN)
        except (NoSuchElementException, TimeoutException):
            pass

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        self.wait_for_element_clickable(element)
        element.click()
        return self

    def fill_input(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_for_new_window_and_load(self, initial_count=None, timeout=10):
        if initial_count is None:
            initial_count = len(self.driver.window_handles)
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > initial_count
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != "about:blank"
        )
        return self
