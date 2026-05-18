import pytest
import allure
from data import FAQData


@pytest.mark.usefixtures("driver", "main_page")
class TestImportantQuestions:

    @allure.title('FAQ: вопрос раскрывается и ответ становится видимым')
    @allure.description(
        'Проверяет UI-поведение: при клике вопрос раскрывается, блок ответа отображается.'
        'Текст ответа не проверяется.'
    )
    @pytest.mark.parametrize("q_index", range(8), ids=[f"Question_{i}" for i in range(8)])
    def test_question_opens_and_shows_answer_ui(self, q_index, driver, main_page):
        driver.refresh()
        main_page.wait_for_accordion_loaded()
        open_result = main_page.ensure_question_is_opened(q_index)
        assert open_result["is_expanded"] and open_result["is_answer_visible"], (
            f"Вопрос {q_index} не раскрылся или ответ не появился."
            f"Раскрыт: {open_result['is_expanded']}, Видим: {open_result['is_answer_visible']}"
        )

    @allure.title('FAQ: текст ответа совпадает с ожидаемым')
    @allure.description(
        'Проверяет контент: текст раскрытого ответа строго соответствует FAQData.ANSWERS.'
    )
    @pytest.mark.parametrize("q_index", range(8), ids=[f"Question_{i}" for i in range(8)])
    def test_answer_text_matches_expected(self, q_index, driver, main_page):
        driver.refresh()
        main_page.wait_for_accordion_loaded()
        main_page.ensure_question_is_opened(q_index)
        actual = main_page.get_answer_text(q_index)
        expected = FAQData.ANSWERS[q_index]
        assert actual == expected, (
            f"Текст ответа для вопроса {q_index} не совпадает.\n"
            f"Ожидалось: {expected}\n"
            f"Получено: {actual}"
        )

    @allure.title('FAQ: открытие нового вопроса автоматически закрывает предыдущий')
    @allure.description(
        "Тест проверяет, что при открытии нового вопроса предыдущий автоматически закрывается. "
        "Каждый прогон проверяет один переход: Question_N → Question_N+1"
    )
    @pytest.mark.parametrize("open_first, open_second, check_closed", [
        (0, 1, 0), (1, 2, 1)], ids=["переход_0-1", "переход_1-2"])
    def test_opening_new_question_closes_previous(self, open_first, open_second, check_closed, driver, main_page):
        driver.refresh()
        main_page.wait_for_accordion_loaded()
        main_page.show_answer(open_first)
        main_page.show_answer(open_second)
        assert main_page.is_question_collapsed(check_closed) is True, (
            f"Question_{check_closed} не закрылся после открытия Question_{open_second}"
        )

