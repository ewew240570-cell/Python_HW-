from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Настройки Firefox (необязательно, но удобно)
options = Options()
options.add_argument("--width=1200")
options.add_argument("--height=800")

driver = webdriver.Firefox(options=options)

try:
    # 1. Открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # 2. Ввести username
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    # 3. Ввести password
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    # 4. Нажать кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # 5. Найти зелёную плашку и вывести её текст
    message = driver.find_element(By.ID, "flash")
    print(message.text.strip())

    time.sleep(2)

finally:
    # 6. Закрыть браузер
    driver.quit()
