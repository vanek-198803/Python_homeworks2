from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.XPATH, "button[@type='submit']")
    login_button.click()

    time.sleep(10)

finally:
    driver.quit()
