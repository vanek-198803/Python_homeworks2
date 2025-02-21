from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        (self._driver.get
         ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

    def wait_for_element(self, by, value):
        return (WebDriverWait(self._driver, 10)
                .until(EC.visibility_of_element_located((by, value))))
