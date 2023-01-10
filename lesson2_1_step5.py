from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

      
link = "https://suninjuly.github.io/math.html"

      
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    

    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-check-custom > label")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-radio-custom > label")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла