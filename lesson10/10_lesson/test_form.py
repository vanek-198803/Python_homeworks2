import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    """Создает экземпляр веб-драйвера Chrome."""
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()

@allure.title("Тест отправки формы")
@allure.description("Проверяет, что форма отправляется корректно.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission(driver: webdriver.Chrome) -> None:
    """Тест отправки формы на странице.

        Args:
            driver (webdriver. Chrome): Экземпляр веб-драйвера Chrome.
        """
    with allure.step("Открыть страницу с формой"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        form_page = FormPage(driver)

    # Данные для заполнения формы
    data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "zip": "",
        "city": "Москва",
        "country": "Россия",
        "job": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнить форму"):
        form_page.fill_form(data)

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Проверить класс поля ZIP-кода"):
        form_page.get_field_class()

    with allure.step("Проверить поля формы"):
        for field_id in data.keys():
            form_page.get_field("field_id")
