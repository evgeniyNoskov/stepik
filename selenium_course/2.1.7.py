from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    imput_value = browser.find_element(By.CSS_SELECTOR, 'img[src="images/chest.png"]')
    x_element = imput_value.get_attribute("valuex")
    # x = x_element.text
    y = calc(x_element)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()    

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()