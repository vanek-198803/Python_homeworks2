from selenium.webdriver.common.by import By
from base_page2 import BasePage


class CalculatorPage(BasePage):
    def set_delay(self, delay):
        delay_input = (self.driver.find_element
                       (By.CSS_SELECTOR, "input#delay"))
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        button = (self.driver.find_element
                  (By.XPATH, f"//span[text()='{button_text}']"))
        button.click()

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
