import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()


def test_form_submission(driver):
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

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

    form_page.fill_form(data)
    form_page.submit_form()
    form_page.get_field_class()
    form_page.get_field("field_id")
