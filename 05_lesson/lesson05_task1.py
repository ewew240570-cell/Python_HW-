from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Настройки браузера
options = Options()
options.add_argument("--start-maximized")

# Укажи путь к chromedriver.exe
service = Service("C:/Users/Евгений/PycharmProjects/Python_HW/05_lesson/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # 2. Найти синюю кнопку по частичному совпадению класса
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    # 3. Клик по кнопке
    blue_button.click()

    # Пауза, чтобы увидеть результат
    time.sleep(2)

finally:
    driver.quit()
