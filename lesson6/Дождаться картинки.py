from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )
sleep(10)
images = driver.find_elements(By.TAG_NAME, "img")
third_image_src = images[2].get_attribute("src")
print(third_image_src)
driver.quit()
