from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time


class TestForm:
    def test_form_validation(self):
        service = Service(
            r"C:\Users\Евгений\PycharmProjects\Python_HW-\msedgedriver.exe"
        )
        driver = webdriver.Edge(service=service)

        try:
            driver.get(
                "https://bonigarcia.dev/selenium"
                "-webdriver-java/data-types.html"
            )
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
            driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']"
            ).click()

            # Ждем немного
            time.sleep(3)

            # Выводим все классы элементов после submit
            print("\n=== Classes after submit ===")
            fields = [
                "first-name", "last-name", "address", "e-mail", "phone",
                "zip-code", "city", "country", "job-position", "company"
            ]

            for field_name in fields:
                try:
                    field = driver.find_element(By.NAME, field_name)
                    print(f"{field_name}: {field.get_attribute('class')}")
                except Exception:
                    print(f"{field_name}: NOT FOUND")

            # Ищем любые сообщения об ошибках
            try:
                alerts = driver.find_elements(By.CLASS_NAME, "alert-danger")
                print(f"\nFound {len(alerts)} alert-danger elements")
            except Exception:
                print("\nNo alert-danger elements found")

        finally:
            driver.quit()


if __name__ == "__main__":
    test = TestForm()
    test.test_form_validation()
