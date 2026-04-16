import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_calculator_07 import CalculatorPage


def test_calculator():
    # Создание и настройка драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        # Создание объекта страницы
        calculator = CalculatorPage(driver)

        # Выполнение действий
        calculator.open()
        calculator.set_delay("45")
        calculator.click_seven()
        calculator.click_plus()
        calculator.click_eight()
        calculator.click_equals()

        # Проверка результата
        result = calculator.wait_for_result("15")
        assert result == "15", f"Expected 15, but got {result}"

        print("✅ Тест пройден! Результат: 15")

    finally:
        # Пауза, чтобы увидеть результат
        time.sleep(5)
        # Закрытие драйвера
        driver.quit()


if __name__ == "__main__":
    test_calculator()
