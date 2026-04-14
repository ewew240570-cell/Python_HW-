import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculator:
    def test_calculator(self):
        # Запуск Google Chrome
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        try:
            # 1. Открыть страницу
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            driver.maximize_window()

            # 2. В поле ввода #delay ввести значение 45
            delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
            delay_input.clear()
            delay_input.send_keys("45")

            # 3. Нажать на кнопки: 7, +, 8, =
            driver.find_element(By.XPATH, "//span[text()='7']").click()
            driver.find_element(By.XPATH, "//span[text()='+']").click()
            driver.find_element(By.XPATH, "//span[text()='8']").click()
            driver.find_element(By.XPATH, "//span[text()='=']").click()

            # 4. Проверить, что в окне отобразится результат 15 через 45 секунд
            # Ожидаем появления результата в дисплее калькулятора
            wait = WebDriverWait(driver, 50)  # ждем до 50 секунд
            result_element = wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
            )

            # Получаем текст результата
            result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
            assert result_text == "15", f"Ожидалось 15, получено {result_text}"

            print("✅ Тест пройден! Результат: 15")

        finally:
            driver.quit()
