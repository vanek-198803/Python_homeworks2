from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_element(By.XPATH,
                                  "//button[contains(text(), "
                                  "'Button Triggering AJAX Request')]")
blue_button.click()

green_message = driver.find_element(By.LINK_TEXT,
                                    "Data loaded with AJAX get request").text
print(green_message)

driver.quit()
