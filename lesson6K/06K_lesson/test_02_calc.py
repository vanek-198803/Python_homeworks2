from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():

    driver = webdriver.Chrome()

    try:
        driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ввод значения в поле по локатору #delay
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.send_keys("45")

        # Нажатие на кнопки
        driver.find_element(By.CSS_SELECTOR, "button#seven").click()
        driver.find_element(By.CSS_SELECTOR, "button#plus").click()
        driver.find_element(By.CSS_SELECTOR, "button#eight").click()
        driver.find_element(By.CSS_SELECTOR, "button#do").click()

        # Ожидание, пока результат не станет видимым
        result_element = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.ID, "result"))
        )

        # Проверка результата
        assert result_element.text == "15", "Результат должен быть 15"

    finally:
        driver.quit()
