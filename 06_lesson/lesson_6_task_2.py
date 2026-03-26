from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

try:

    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    updated_button = driver.find_element(By.ID, "updatingButton")
    button_text = updated_button.text

    print("Текст кнопки после изменения:", button_text)

    expected_text = "SkyPro"
    if button_text == expected_text:
        print("✅ Тест пройден: текст кнопки изменился на 'SkyPro'")
    else:
        print(f"❌ Тест не пройден: ожидалось '{expected_text}', получено '{button_text}'")

finally:

    driver.quit()
