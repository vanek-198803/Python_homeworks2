from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Укажите путь к вашему драйверу
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Находим кнопку "Add Element" и кликаем на нее 5 раз
    add_element_button = driver.find_element(By.XPATH,
                                             "//button[text()='Add Element']")
    for _ in range(5):
        add_element_button.click()

    # Ждем немного, чтобы элементы успели добавиться
    time.sleep(5)

    # Собираем список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH,
                                          "//button[text()='Delete']")

    # Выводим размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрываем браузер
    driver.quit(None)
