from selenium.webdriver.common.by import By

class MainLocators:
    COOKIE_ACCEPT_BTN = [By.ID, "rcc-confirm-button"]
    LOGO_SAMOKAT = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    LOGO_YANDEX = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    SAMOKAT_PAGE_ELEMENT = [By.CLASS_NAME, "Home_Header__iJKdX"]
    YANDEX_PAGE_ELEMENT = [By.XPATH, "//textarea[contains(@placeholder, 'Найдётся всё')]"]
    YANDEX_PAGE_ALTERNATIVE_ELEMENT = [By.XPATH, "//a[@aria-label='Yandex']"]
