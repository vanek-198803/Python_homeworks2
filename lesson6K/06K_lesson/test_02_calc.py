from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():

    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения в поле по локатору #delay
    delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay.clear()
    delay.send_keys("45")

    # Нажатие на кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание, пока результат не станет видимым
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15
    driver.quit()
