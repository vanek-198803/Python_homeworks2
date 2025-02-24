from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage3:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by: str, value: str):
        """Ожидает элемент на странице."""
        return (WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((by, value))))

    def click(self, by: str, value: str) -> None:
        """Кликает на элемент."""
        self.wait_for_element(by, value).click()

    def send_keys(self, by: str, value: str, text: str) -> None:
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: str, value: str) -> str:
        """Получает текст элемента."""
        return self.wait_for_element(by, value).text
