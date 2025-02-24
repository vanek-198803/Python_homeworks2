from selenium.webdriver.common.by import By
from basepage3 import BasePage3


class CheckoutPage(BasePage3):

    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя в поле ввода."""
        self.send_keys(By.ID, "first-name", first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию в поле ввода."""
        self.send_keys(By.ID, "last-name", last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Вводит почтовый код в поле ввода."""
        self.send_keys(By.ID, "postal-code", postal_code)

    def click_continue(self) -> None:
        """Вводит почтовый код в поле ввода."""
        self.click(By.XPATH, "//input[@type='submit']")

    def get_total(self) -> str:
        """Получает итоговую сумму из поля."""
        return self.get_text(By.CSS_SELECTOR, ".summary_total_label")
