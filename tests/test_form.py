import pytest
import allure
from src.charset import charset
from src.form import Form

@allure.parent_suite('Authorisation')
@allure.suite('Register/Login jobs')
@allure.testcase('https://app.qase.io/project/QUAL?case=2', 'QUAL-2')

@allure.description('[Form][Auth][Positive][Func] Test of the form')
@pytest.mark.parametrize('username', [charset(6)])
@pytest.mark.parametrize('password', [charset(20, True, True)])
@allure.title('Form')
def test_form(driver, username, password):

    allure.dynamic.parameter('username', username)
    allure.dynamic.parameter('password', password)
#   Register
    with allure.step('User registration form'):
        print('\nFilling register form')
        register = Form.fill_register(driver, username, password)
        if register:
            pass

#   Login
    with allure.step('User login form'):
        print('\nFilling login form')
        login = Form.fill_login(driver, username, password)
        if login:
            pass
