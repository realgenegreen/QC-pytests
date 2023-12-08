from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Form():

    @staticmethod
    def fill_register(driver, username, password):

        driver.get('http://localhost:8080/register')
        input_1 = driver.find_element(By.CSS_SELECTOR, value='#username')
        input_1.click()
        input_1.send_keys(username)
        input_2 = driver.find_element(By.CSS_SELECTOR, value='#password')
        input_2.click()
        input_2.send_keys(password)
        button =  driver.find_element(By.CSS_SELECTOR, value='.register-btn')
        button.click()
        element = driver.find_element(By.CSS_SELECTOR, value='.user-card')
        assert 'Ошибка' not in element.text
        current_url = driver.current_url
        WebDriverWait(driver, 100).until(EC.url_changes(current_url))
        if driver.find_element(By.CSS_SELECTOR, value='.sidebar'):
            print('Register succsess')
        else:
            print('Failed! Bug located')

    @staticmethod
    def fill_login(driver, username, password):

        driver.get('http://localhost:8080/login')

        input_1 = driver.find_element(By.CSS_SELECTOR, value='#username')
        input_1.click()
        input_1.send_keys(username)
        input_2 = driver.find_element(By.CSS_SELECTOR, value='#password')
        input_2.click()
        input_2.send_keys(password)
        button =  driver.find_element(By.CSS_SELECTOR, value='.login-btn')
        button.click()
        element = driver.find_element(By.CSS_SELECTOR, value='div.d-flex:nth-child(2)')
        assert 'Неверная' not in element.text
        current_url = driver.current_url
        WebDriverWait(driver, 100).until(EC.url_changes(current_url))
        if driver.find_element(By.CSS_SELECTOR, value='.sidebar'):
            print('Login succsess')
        else:
            print('Failed! Bug located')
