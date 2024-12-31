from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Находим синюю кнопку и кликаем по ней
    blue_button = driver.find_element(By.CSS_SELECTOR,
                                      'button.btn.btn-primary')
    blue_button.click()

    time.sleep(5)

finally:
    driver.quit()
