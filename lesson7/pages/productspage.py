from selenium.webdriver.common.by import By
from basepage3 import BasePage3


class ProductsPage(BasePage3):
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self, ID):
        (self._driver.find_element
         (By.ID, f'add-to-cart-{ID}').click())

    def go_to_cart(self):
        (self._driver.find_element
         (By.XPATH, "//a[@class='shopping_cart_link']").click())

    def go_to_carts(self):
        (self._driver.find_element
         (By.XPATH, "//button[text()='Checkout']").click())
