from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BTN_TOP = [By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"]
    ORDER_BTN_BOTTOM = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]"]

    NAME = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    SURNAME = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    ADDRESS = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    STATION_INPUT = [By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"]
    STATION_OPTION_TEMPLATE = "//button[contains(@class, 'Order_SelectOption')]//div[contains(text(), '{}')]" 
    PHONE = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"]
    NEXT_BTN = [By.XPATH, ".//div[contains(@class, 'Order_NextButton')]/button[contains(@class, 'Button_Button')]"]

    DELIVERY_DATE = [By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]"]
    DURATION_DROPDOWN = [By.XPATH, "//div[contains(@class, 'Dropdown-root')]"]
    DURATION_OPTION_TEMPLATE = "//div[contains(@class, 'Dropdown-option') and text()='{}']"
    COLOR_BLACK = [By.ID, "black"]
    COLOR_GREY = [By.ID, "grey"]
    COMMENT = [By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]"]
    ORDER_BTN = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]"]

    CONFIRMATION_BTN = [By.XPATH, "//button[contains(text(), 'Да')]"]
    ORDER_MODAL = [By.XPATH, "//div[contains(@class, 'Order_Modal') and contains(., 'Заказ оформлен')]"]
    STATUS_BTN = [By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Посмотреть статус']"]

    @staticmethod
    def get_station_option(station_name):
        return [By.XPATH, OrderLocators.STATION_OPTION_TEMPLATE.format(station_name)]

    @staticmethod
    def get_duration_option(duration_text):
        return [By.XPATH, OrderLocators.DURATION_OPTION_TEMPLATE.format(duration_text)]
