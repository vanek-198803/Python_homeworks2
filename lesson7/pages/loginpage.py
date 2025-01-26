from selenium.webdriver.common.by import By
from basepage3 import BasePage3


class LoginPage(BasePage3):
    def enter_username(self, username):
        self.send_keys(By.ID, "user-name", username)

    def enter_password(self, password):
        self.send_keys(By.ID, "password", password)

    def click_login(self):
        self.click(By.XPATH, "//input[@type='submit']")
