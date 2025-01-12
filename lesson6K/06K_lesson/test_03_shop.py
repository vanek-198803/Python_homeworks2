from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart():
    driver = webdriver.Chrome()

    try:
        # Открытие веб-страницы
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Добавление товаров в корзину
        (driver.find_element(By.XPATH, "//div[text()='Sauce "
                                       "Labs Backpack']/ancestor:"
                                       ":div[@class='inventory_item']/"
                                       "/button").click())
        (driver.find_element(By.XPATH, "//div[text()='Sauce"
                                       " Labs Bolt T-Shirt']/ancestor::div"
                                       "[@class='inventory_item']/"
                                       "/button").click())
        (driver.find_element(By.XPATH, "//div[text()='Sauce "
                                       "Labs Onesie']/ancestor:"
                                       ":div[@class='inventory_item']/"
                                       "/button").click())
        # Переход в корзину
        (driver.find_element(By.XPATH, "//a[@class='"
                                       "shopping_cart_link']").click())
        # Нажатие на Checkout
        driver.find_element(By.XPATH, "//button[text()='Checkout']").click()

        # Заполнение формы данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Нажатие на кнопку Continue
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Ожидание, пока итоги не станут видимыми
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".summary_total_label"))
        )

        # Проверка итоговой суммы
        assert (total_element.text ==
                "Total: $58.29"), "Итоговая сумма должна быть $58.29"

    finally:
        driver.quit()
