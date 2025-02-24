from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.chrome import webdriver

class BasePage:
    def __init__(self, driver: webdriver) -> None:
        """Инициализирует базовый класс страницы.

               Args:
                   driver (webdriver): Экземпляр веб-драйвера.
               """

        self._driver = driver
        (self._driver.get
         ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

    def wait_for_element(self, by: str, value: str) -> webdriver. WebElement:
        """Ожидает появления элемента на странице.

               Args:
                   by (str): Метод поиска элемента.
                   value (str): Значение для поиска элемента.

               Returns:
                   webdriver.WebElement: Найденный элемент.
               """
        return (WebDriverWait(self._driver, 10)
                .until(EC.visibility_of_element_located((by, value))))
