from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage3:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        return (WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((by, value))))

    def click(self, by, value):
        self.wait_for_element(by, value).click()

    def send_keys(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return self.wait_for_element(by, value).text
