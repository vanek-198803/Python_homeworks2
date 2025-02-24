from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Инициализирует базовую страницу с веб-драйвером.

        Args:
        driver (webdriver): Веб-драйвер, который будет использоваться на странице.
        """
        self.driver = driver

    def wait_for_element(self, by: str, value: str):
        """
        Ожидает, когда элемент станет видимым на странице.

        Args:
        by (str): Способ нахождения элемента (например, By.ID).
        value (str): Значение, по которому будет происходить поиск элемента.

        Returns:
        WebElement: Ожидаемый элемент.
        """
        return (WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((by, value))))

    def wait_for_text(self, by: str, value: str, text: str, timeout: int = 10):
        """
        Ожидает, когда текст появится в элементе.

        Args:
         by (str): Способ нахождения элемента.
        value (str): Значение, по которому будет происходить поиск элемента.
        text (str): Текст, который должен появиться в элементе.
        timeout (int): Время в секундах для ожидания.

        Returns:
        None
        """
        (WebDriverWait(self.driver, timeout)
         .until(EC.text_to_be_present_in_element((by, value), text)))
