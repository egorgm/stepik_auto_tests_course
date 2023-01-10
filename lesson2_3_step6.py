from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

      
link = "http://suninjuly.github.io/redirect_accept.html"

      
try:
    browser = webdriver.Chrome()
    browser.get(link)
        
    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла