from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds):
        """Установить задержку"""
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_seven(self):
        """Нажать кнопку 7"""
        self.driver.find_element(*self.BUTTON_7).click()

    def click_eight(self):
        """Нажать кнопку 8"""
        self.driver.find_element(*self.BUTTON_8).click()

    def click_plus(self):
        """Нажать кнопку +"""
        self.driver.find_element(*self.BUTTON_PLUS).click()

    def click_equals(self):
        """Нажать кнопку ="""
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def wait_for_result(self, expected_value):
        """Ожидать появления результата"""
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_value)
        )
        return self.driver.find_element(*self.SCREEN).text
