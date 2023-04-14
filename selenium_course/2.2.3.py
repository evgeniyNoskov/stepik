from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    sum = num1 + num2
    # print(sum)

    select = browser.find_element(By.TAG_NAME, "select")
    select.click()

    input = browser.find_element(By.CSS_SELECTOR, "option[value='"+str(sum)+"']")
    input.click()


    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()