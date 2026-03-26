from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
try:
    driver.get("http://uitestingplayground.com/ajax")
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()
    print("Кнопка нажата, ожидание загрузки данных...")
    wait = WebDriverWait(driver, 20)
    success_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    message_text = success_element.text
    print("Текст из зеленой плашки:", message_text)
finally:
    driver.quit()
