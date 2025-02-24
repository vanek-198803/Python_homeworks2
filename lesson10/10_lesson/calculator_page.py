from selenium.webdriver.common.by import By
from base_page2 import BasePage


class CalculatorPage(BasePage):
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку в калькуляторе.

        Args:
        delay (str): Задержка в секундах, которую нужно установить.

        Returns:
        None
        """
        delay_input = (self.driver.find_element
                       (By.CSS_SELECTOR, "input#delay"))
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        Args:
        button_text (str): Текст кнопки, на которую нужно нажать.

        Returns:
        None
        """
        button = (self.driver.find_element
                  (By.XPATH, f"//span[text()='{button_text}']"))
        button.click()

    def get_result(self) -> str:
        """
        Получает результат операции из калькулятора.

        Returns:
        str: Результат, отображаемый на экране калькулятора.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
