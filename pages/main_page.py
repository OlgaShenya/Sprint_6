from pages.base_page import BasePage
from locators.important_questions_locators import ImportantQuestionsLocators
from data import FAQData
import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPage(BasePage):

    def _get_question_element(self, index):
        questions = self.driver.find_elements(*ImportantQuestionsLocators.ACCORDION_QUESTION)
        return questions[index]

    def _get_answer_element(self, index):
        answers = self.driver.find_elements(*ImportantQuestionsLocators.ACCORDION_ANSWER)
        return answers[index]

    @allure.step("Ожидание загрузки аккордеона с вопросами")
    def wait_for_accordion_loaded(self):
        self.wait_for_element_located(ImportantQuestionsLocators.ACCORDION_QUESTION)

    @allure.step("Раскрыть ответ на вопрос с индексом {index}")
    def show_answer(self, index):
        question = self._get_question_element(index)
        self.scroll_to_center(question)
        self.wait_for_element_clickable(question)
        question.click()
    
    @allure.step("Проверка видимости ответа с индексом {index}")
    def is_answer_visible(self, index):
        answer = self._get_answer_element(index)
        self.scroll_to_center(answer)
        self.wait_for_element_visible(answer)
        return answer.is_displayed()
    
    @allure.step("Проверка, что вопрос с индексом {index} раскрыт (aria-expanded='true')")
    def is_question_expanded(self, index):
        question = self._get_question_element(index)
        state = question.get_attribute("aria-expanded")
        return state == "true"

    @allure.step("Проверка, что вопрос с индексом {index} свёрнут (aria-expanded='false')")
    def is_question_collapsed(self, index):
        if index > 0:
            question = self._get_question_element(index-1)
            state = question.get_attribute("aria-expanded")
            return state == "false"
        return True

    @allure.step("Гарантировать, что вопрос с индексом {index} открыт и ответ виден")
    def ensure_question_is_opened(self, index):
        self.show_answer(index)
        return {
            "is_expanded": self.is_question_expanded(index),
            "is_answer_visible": self.is_answer_visible(index),
        }

    @allure.step("Получить текст ответа с индексом {index}")
    def get_answer_text(self, index):
        answer = self._get_answer_element(index)
        self.scroll_to_center(answer)
        self.wait_for_element_visible(answer)
        return answer.text.strip()

    @allure.step("Проверить, что текст ответа с индексом {index} соответствует ожидаемому")
    def is_answer_text_correct(self, index):
        actual = self.get_answer_text(index)
        expected = FAQData.ANSWERS[index]
        return actual == expected

    @allure.step("Раскрыть вопрос {index} и проверить текст ответа")
    def verify_answer_for_question(self, index):
        self.show_answer(index)
        actual = self.get_answer_text(index)
        expected = FAQData.ANSWERS[index]
        return {
            "is_correct": actual == expected,
            "actual": actual,
            "expected": expected,
        }

    @allure.step("Переключение на новую вкладку")
    def switch_tab_if_needed(self, opens_new_tab):
        """Тонкая обёртка: вызывает переключение только если сценарий требует новой вкладки."""
        if opens_new_tab:
            self.wait_for_new_window_and_load(initial_count=1) # исходное количество вкладок 1, ждем когда станет больше

    @allure.step("Поиск первого видимого элемента из списка")
    def find_first_displayed_element(self, locators, timeout = 10):
        """Ищет первый видимый элемент из списка. Делегирует ожидание видимости в BasePage."""
        for loc in locators:
            try:
                self.wait_for_element_located(loc, timeout)
                elem = self.driver.find_element(*loc)
                self.wait_for_element_visible(elem, timeout)
                return elem
            except (TimeoutException, NoSuchElementException):
                continue
        return None
