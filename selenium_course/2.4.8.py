from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 45).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    
    button.click()
    
    browser.execute_script("window.scrollBy(0, 300);")

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    browser.find_element(By.ID, "solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()