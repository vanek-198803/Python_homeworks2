from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        return (WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((by, value))))

    def wait_for_text(self, by, value, text, timeout=10):
        (WebDriverWait(self.driver, timeout)
         .until(EC.text_to_be_present_in_element((by, value), text)))
