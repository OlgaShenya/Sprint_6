from selenium.webdriver.common.by import By

class ImportantQuestionsLocators:
    ACCORDION_QUESTION = [By.XPATH, "//div[contains(@id,'accordion__heading-')]"]
    ACCORDION_ANSWER = [By.XPATH, "//div[contains(@id,'accordion__panel-')]"]
