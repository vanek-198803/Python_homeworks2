import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
from selenium.webdriver.common.by import By

@pytest.fixture
def driver() -> webdriver.Chrome:
    """
    Создает экземпляр веб-драйвера Chrome и завершается после выполнения теста.

    Returns:
        webdriver.Chrome: Экземпляр веб-драйвера Chrome.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Тест медленного калькулятора")
@allure.description("Проверяет работу медленного калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver: webdriver.Chrome) -> None:
    """
    Тест на проверку работы медленного калькулятора.

    Args:
        driver (webdriver.Chrome): Веб-драйвер Chrome.

    Returns:
        None
    """
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page = CalculatorPage(driver)

    with allure.step("Установка задержки"):
        calculator_page.set_delay("45")

    with allure.step("Нажатие на кнопки для вычисления"):
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

    with allure.step("Ожидание результата"):
        calculator_page.wait_for_text(By.CSS_SELECTOR, ".screen", "15", timeout=46)

    with allure.step("Проверка результата"):
        result = calculator_page.get_result()
        assert int(result) == 15

