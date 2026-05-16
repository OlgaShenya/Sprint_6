import pytest
import allure
from data import FAQData


@pytest.mark.usefixtures("driver", "main_page")
class TestImportantQuestions:
    @allure.title('FAQ: вопрос раскрывается и отображает корректный ответ')
    @allure.description(
        'Для каждого из 8 вопросов проверяется: вопрос раскрыт, ответ виден, текст ответа совпадает с FAQData.ANSWERS'
    )
    @pytest.mark.parametrize("q_index", range(8), ids=[f"Question_{i}" for i in range(8)])
    def test_faq_question_opens_with_correct_answer(self, q_index, driver, main_page):
        driver.refresh()
        main_page.wait_for_accordion_loaded()
        open_result = main_page.ensure_question_is_opened(q_index)
        assert open_result["is_expanded"], f"Вопрос {q_index} не раскрылся"
        assert open_result["is_answer_visible"], f"Ответ {q_index} не появился"
        actual = main_page.get_answer_text(q_index)
        expected = FAQData.ANSWERS[q_index]
        assert actual == expected, (
            f"Текст ответа для вопроса {q_index} не совпадает.\n"
            f"Ожидалось: {expected}\n"
            f"Получено: {actual}"
        )

    @allure.title('FAQ: открытие нового вопроса автоматически закрывает предыдущий')
    @allure.description("Тест проверяет корректную работу аккордеона FAQ: при клике на новый вопрос "
    "предыдущий открытый ответ должен автоматически сворачиваться. "
    "Проверяется последовательность: Question_0 → Question_1 (проверка Q0) → Question_2 (проверка Q1).")
    def test_opening_new_question_closes_previous(self, driver, main_page):
        driver.refresh()
        main_page.wait_for_accordion_loaded()
        main_page.show_answer(0)
        main_page.show_answer(1)
        assert main_page.is_question_collapsed(0) is True, "Question_0 не закрылся после открытия Question_1"
        main_page.show_answer(2)
        assert main_page.is_question_collapsed(1) is True, "Question_1 не закрылся после открытия Question_2"
