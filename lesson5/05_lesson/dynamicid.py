from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Находим синюю кнопку и кликаем по ней
    blue_button = driver.find_element(By.CSS_SELECTOR,
                                      "button[class^='btn btn-primary']")
    blue_button.click()

    time.sleep(5)

finally:
    # Закрываем браузер
    driver.quit()
