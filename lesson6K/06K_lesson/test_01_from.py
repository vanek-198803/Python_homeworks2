from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_from():
    driver = webdriver.Chrome()

    # Открытие веб-страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
    driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
    driver.find_element(By.NAME, 'zip-code').send_keys("")
    driver.find_element(By.NAME, 'city').send_keys("Москва")
    driver.find_element(By.NAME, 'country').send_keys("Россия")
    driver.find_element(By.NAME, 'job-position').send_keys("QA")
    driver.find_element(By.NAME, 'company').send_keys("SkyPro")

    # Нажатие кнопки Submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    # Ожидание, пока элементы не станут доступными
    (WebDriverWait(driver, 10).
     until(EC.visibility_of_element_located((By.ID, "zip-code"))))
    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

    assert "success" in driver.find_elements(By.ID, '[firstName, lastName, address, email, phone, city, country, job, company]').get_attribute("class")
    # не могу понять, как проверить ысе ячейки зеленого цвета


    driver.quit()
