from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_from():
    driver = webdriver.Chrome()

    try:
        # Открытие веб-страницы
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение формы
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='firstName']").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='lastName']").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='address']").send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='email']").send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='phone']").send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='zip-code']").send_keys("")
        # Оставляем Zip code пустым
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='city']").send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='country']").send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='jobPosition']").send_keys("QA")
        driver.find_element(By.CSS_SELECTOR,
                            "input[name='company']").send_keys("SkyPro")

        # Нажатие кнопки Submit
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        # Ожидание, пока элементы не станут доступными
        (WebDriverWait(driver, 10).
         until(EC.visibility_of_element_located((By.NAME, "zip"))))

        # Проверка цвета поля Zip code
        zip_element = driver.find_element(By.NAME, "zip")
        assert "red" in zip_element.get_attribute("style"), \
            "Zip code должен быть подсвечен красным"

        # Проверка, что остальные поля подсвечены зеленым
        fields = ["firstName", "lastName", "address",
                  "email", "phone", "city", "country",
                  "jobPosition", "company"]
        for field in fields:
            element = driver.find_element(By.NAME, field)
            assert "green" in element.get_attribute("style"), \
                f"{field} должен быть подсвечен зеленым"

    finally:
        driver.quit()
