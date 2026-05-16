# Sprint_6

# Автотесты для сервиса «Самокат»

Учебный проект — автоматизированное тестирование веб-приложения [Самокат](https://qa-scooter.education-services.ru/) с использованием **Selenium**, **pytest** и **Allure**.

## Стек

- Python 3
- Selenium 4
- pytest
- Allure Report
- Firefox (WebDriver)

## Структура проекта

```
.
├── conftest.py                          # фикстуры: driver, main_page, order_page
├── data.py                              # тестовые данные (FAQData.ANSWERS)
├── locators/                            # локаторы элементов
│   ├── main_locators.py                 # главная: куки, логотипы
│   ├── important_questions_locators.py  # FAQ-аккордеон
│   └── order_locators.py                # форма заказа
├── pages/                               # Page Object
│   ├── base_page.py                     # общие действия (wait, click, scroll)
│   ├── main_page.py                     # главная страница и FAQ
│   └── order_page.py                    # сценарий заказа
├── tests/
│   ├── test_important_questions_page.py # FAQ
│   ├── test_logo_navigation_page.py     # логотипы
│   └── test_order_page.py               # заказ
├── requirements.txt
└── .gitignore
```

## Покрытие тестами

| Модуль | Что проверяется |
| ------ | --------------- |
| `test_important_questions_page` | Раскрытие 8 вопросов FAQ, корректный текст ответа (`FAQData.ANSWERS`); при открытии нового вопроса предыдущий сворачивается |
| `test_logo_navigation_page` | Переход по логотипу Самоката; переход по логотипу Яндекса (новая вкладка) |
| `test_order_page` | Полный позитивный сценарий заказа через верхнюю и нижнюю кнопку «Заказать» |

Архитектура: **Page Object Model** — локаторы, действия на страницах, тестовые данные и сценарии в тестах разделены.

## Установка

1. Клонируйте репозиторий и перейдите в каталог проекта.

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
```

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Установите [Firefox](https://www.mozilla.org/firefox/) и убедитесь, что `geckodriver` доступен в `PATH` (для Selenium 4 менеджер драйверов часто подтягивает его автоматически).

## Запуск тестов

Все тесты:

```bash
pytest
```

Конкретный файл:

```bash
pytest tests/test_order_page.py -v
pytest tests/test_important_questions_page.py -v
pytest tests/test_logo_navigation_page.py -v
```

С генерацией результатов для Allure:

```bash
pytest --alluredir=allure-results
```

## Allure-отчёт

После прогона с `--alluredir`:

```bash
allure serve allure-results
```

Откроется локальный отчёт с шагами, заголовками и описаниями тестов.

## Примечания

- Базовый URL задаётся в `conftest.py`: `https://qa-scooter.education-services.ru/`
- По умолчанию используется **Firefox** (`webdriver.Firefox()`)
- Фикстура `main_page` открывает главную страницу и возвращает объект `MainPage`
- Перед сценариями заказа и навигации по логотипам баннер cookies принимается автоматически, если он отображается
