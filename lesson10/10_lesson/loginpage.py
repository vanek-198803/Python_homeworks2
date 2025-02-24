from selenium.webdriver.common.by import By
from basepage3 import BasePage3


class LoginPage(BasePage3):
    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя в поле ввода."""
        self.send_keys(By.ID, "user-name", username)

    def enter_password(self, password: str) -> None:
        """Вводит пароль в поле ввода."""
        self.send_keys(By.ID, "password", password)

    def click_login(self) -> None:
        """Нажимает кнопку входа."""
        self.click(By.XPATH, "//input[@type='submit']")
