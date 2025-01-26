from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")

    # Вводим тест 1000
    input_field.send_keys("1000")
    time.sleep(5)

    # Очищаем поле
    input_field.clear()
    time.sleep(3)

    # Вводим текст 999
    input_field.send_keys("999")
    time.sleep(3)

finally:
    driver.quit()
