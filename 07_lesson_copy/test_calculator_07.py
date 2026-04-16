import time
from page_calculator_07 import CalculatorPage


def test_calculator(chrome_driver):
    """Тест калькулятора с использованием фикстуры"""
    calculator = CalculatorPage(chrome_driver)
    calculator.open()
    calculator.set_delay("5")
    calculator.click_seven()
    calculator.click_plus()
    calculator.click_eight()
    calculator.click_equals()

    result = calculator.wait_for_result("15")
    assert result == "15", f"Expected 15, but got {result}"

    print("✅ Тест пройден! Результат: 15")
    time.sleep(3)
