from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, first_name):
        """Заполнить имя"""
        field = self.driver.find_element(*self.FIRST_NAME_INPUT)
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        """Заполнить фамилию"""
        field = self.driver.find_element(*self.LAST_NAME_INPUT)
        field.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        """Заполнить почтовый индекс"""
        field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        field.send_keys(postal_code)

    def fill_form(self, first_name, last_name, postal_code):
        """Заполнить всю форму"""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)

    def click_continue(self):
        """Нажать кнопку Continue"""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_text(self):
        """Получить текст итоговой стоимости"""
        total = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return total.text

    def get_total_value(self):
        """Получить числовое значение итоговой стоимости"""
        text = self.get_total_text()
        # Извлекаем сумму из текста "Total: $58.29"
        return text.replace("Total: ", "")
