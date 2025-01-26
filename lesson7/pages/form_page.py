from selenium.webdriver.common.by import By
from base_page import BasePage


class FormPage(BasePage):
    def fill_form(self, data):
        (self._driver.find_element
         (By.NAME, "first-name").send_keys(data["first_name"]))
        (self._driver.find_element
         (By.NAME, "last-name").send_keys(data["last_name"]))
        (self._driver.find_element
         (By.NAME, "address").send_keys(data["address"]))
        (self._driver.find_element
         (By.NAME, "e-mail").send_keys(data["email"]))
        (self._driver.find_element
         (By.NAME, "phone").send_keys(data["phone"]))
        (self._driver.find_element
         (By.NAME, "zip-code").send_keys(data["zip"]))
        (self._driver.find_element
         (By.NAME, "city").send_keys(data["city"]))
        (self._driver.find_element
         (By.NAME, "country").send_keys(data["country"]))
        (self._driver.find_element
         (By.NAME, "job-position").send_keys(data["job"]))
        (self._driver.find_element
         (By.NAME, "company").send_keys(data["company"]))

    def submit_form(self):
        (self._driver.find_element
         (By.XPATH, "//button[text()='Submit']").click())

    def get_field_class(self,):
        self._driver.find_element(By.ID, "zip-code").get_attribute("class")

    def get_field(self, field_id):
        fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]
        for field_id in fields:
            self._driver.find_element(By.ID, field_id)
            assert ("success" in self._driver.find_element(By.ID, field_id)
                    .get_attribute("class")), (f"Поле {field_id} "
                                               f"должно быть подсвечено"
                                               f" зеленым")
