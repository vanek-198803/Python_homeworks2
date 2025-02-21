from selenium.webdriver.common.by import By
from basepage3 import BasePage3


class CheckoutPage(BasePage3):

    def enter_first_name(self, first_name):
        self.send_keys(By.ID, "first-name", first_name)

    def enter_last_name(self, last_name):
        self.send_keys(By.ID, "last-name", last_name)

    def enter_postal_code(self, postal_code):
        self.send_keys(By.ID, "postal-code", postal_code)

    def click_continue(self):
        self.click(By.XPATH, "//input[@type='submit']")

    def get_total(self):
        return self.get_text(By.CSS_SELECTOR, ".summary_total_label")
