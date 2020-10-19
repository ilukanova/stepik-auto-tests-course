from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys('Ivan')
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys('Ivanov')
    email = browser.find_element(By.NAME, "email")
    email.send_keys('test@test.ru')

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
