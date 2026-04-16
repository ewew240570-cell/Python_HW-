from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        """Ввести имя пользователя"""
        field = self.driver.find_element(*self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль"""
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        """Нажать кнопку входа"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username, password):
        """Выполнить авторизацию"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
