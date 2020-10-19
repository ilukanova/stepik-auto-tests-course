from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.ID, "num1")
    x1 = x1_element.text
    x2_element = browser.find_element(By.ID, "num2")
    x2 = x2_element.text
    y = str(int(x1) + int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


