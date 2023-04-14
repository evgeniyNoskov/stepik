import pytest
import time 
import math
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # browser.implicitly_wait(600)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('idLess', ['236895','236896','236897','236898','236899','236903','236904','236905'])
def test_guest_should_see_login_link(browser, idLess):
    with open('cred.json', 'r') as file:
        cred = json.load(file)
    
    link = f"https://stepik.org/lesson/{idLess}/step/1"
    # link = f"https://stepik.org/lesson/236896/step/1"
    browser.get(link)
    print('перешли на страницу')
    loginBtn = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    loginBtn.click()
    print('открыли страницу авторизации')

    inputLogin = browser.find_element(By.CSS_SELECTOR, "input#id_login_email")
    inputLogin.send_keys(cred['login'])
    inputPassword = browser.find_element(By.CSS_SELECTOR, "input#id_login_password")
    inputPassword.send_keys(cred['password'])
    login = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    login.click()
    print('авторизовались')

    

    # current_url = browser.current_url

    # assert current_url == 'https://stepik.org/lesson/236895/step/1?auth=login'

    # print(answer)

    awaitElem = WebDriverWait(browser, 190).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.ember-text-area'))
    )
    answerField = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
    answerField.click()

    answer = math.log(int(time.time()))
    
    answerField.send_keys(str(answer))
    print('заполнили поле')

    # time.sleep(30)
    # submitBtn = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')

    submitBtn = WebDriverWait(browser, 190).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
    )
    submitBtn.click()
    print('отправили ответ')

    result = WebDriverWait(browser, 190).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint"))
    )
    # result = browser.find_element("p.smart-hints__hint")
    assert result.text == 'Correct!', 'Text should be "Correct!", but they '+result.text
    print('получили ответ')

    
    
