import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))
    calculator_page = CalculatorPage(driver)

    # Установка задержки
    calculator_page.set_delay("45")

    # Нажатие на кнопки
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')

    # Ожидание результата
    (calculator_page.wait_for_text
     (By.CSS_SELECTOR, ".screen", "15", timeout=46))

    # Проверка результата
    result = calculator_page.get_result()
    assert int(result) == 15
