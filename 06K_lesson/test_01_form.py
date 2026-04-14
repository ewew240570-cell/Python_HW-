import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service


class TestForm:
    def test_form_validation(self):
        service = Service(r"C:\Users\Евгений\PycharmProjects\Python_HW-\msedgedriver.exe")
        driver = webdriver.Edge(service=service)

        try:
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
            driver.maximize_window()

            # Заполнение формы
            driver.find_element(By.NAME, "first-name").send_keys("Иван")
            driver.find_element(By.NAME, "last-name").send_keys("Петров")
            driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
            driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
            driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
            driver.find_element(By.NAME, "zip-code").send_keys("")
            driver.find_element(By.NAME, "city").send_keys("Москва")
            driver.find_element(By.NAME, "country").send_keys("Россия")
            driver.find_element(By.NAME, "job-position").send_keys("QA")
            driver.find_element(By.NAME, "company").send_keys("SkyPro")

            # Нажатие кнопки
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            # Ожидание результатов валидации
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))

            # Проверка: поле Zip code подсвечено красным (с ожиданием)
            zip_field = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
            zip_class = zip_field.get_attribute("class")
            assert "danger" in zip_class or "error" in zip_class

            # Проверка остальных полей
            fields = ["first-name", "last-name", "address", "e-mail", "phone",
                      "city", "country", "job-position", "company"]
            for field_name in fields:
                field = driver.find_element(By.NAME, field_name)
                field_class = field.get_attribute("class")
                assert "success" in field_class or "valid" in field_class

            print("✅ Все проверки пройдены успешно!")

        finally:
            driver.quit()
