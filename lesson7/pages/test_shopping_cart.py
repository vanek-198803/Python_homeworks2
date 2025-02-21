import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson7.pages.loginpage import LoginPage
from lesson7.pages.productspage import ProductsPage
from lesson7.pages.checkoutpage import CheckoutPage


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Работа со страницами
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(driver)
    products_page.add_to_cart("sauce-labs-backpack")
    products_page.add_to_cart("sauce-labs-bolt-t-shirt")
    products_page.add_to_cart("sauce-labs-onesie")
    products_page.go_to_cart()
    products_page.go_to_carts()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("Иван")
    checkout_page.enter_last_name("Петров")
    checkout_page.enter_postal_code("123456")
    checkout_page.click_continue()

# Проверка итоговой суммы
    total = checkout_page.get_total()
    assert total == "Total: $58.29", \
        "Итоговая сумма должна быть $58.29"
