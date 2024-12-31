from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/entry_ad")

    time.sleep(5)

    close_button = driver.find_element(By.XPATH,
                                       "//div[modal-footer='Close']/")
    close_button.click()

    time.sleep(5)

finally:
    driver.quit()
