import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from loginpage import LoginPage
from productspage import ProductsPage
from checkoutpage import CheckoutPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    """Создает экземпляр веб-драйвера Chrome."""
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()

@allure.title("Тест корзины покупок")
@allure.description("Проверяет работу корзины покупок на сайте.")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.NORMAL)

def test_shopping_cart(driver: webdriver.Chrome) -> None:
    """Тест на проверку процесса покупки товаров."""
    driver.get("https://www.saucedemo.com/")

    with allure.step("Ввод имени пользователя и пароля"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        products_page = ProductsPage(driver)
        products_page.add_to_cart("sauce-labs-backpack")
        products_page.add_to_cart("sauce-labs-bolt-t-shirt")
        products_page.add_to_cart("sauce-labs-onesie")
        products_page.go_to_cart()
        products_page.go_to_carts()

    with allure.step("Проверка оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("Иван")
        checkout_page.enter_last_name("Петров")
        checkout_page.enter_postal_code("123456")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой суммы"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29", \
        "Итоговая сумма должна быть $58.29"
