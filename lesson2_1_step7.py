from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

      
link = "http://suninjuly.github.io/get_attribute.html"

      
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    sunduk = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = sunduk.get_attribute("valuex")
    y = calc(x)
    

    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла