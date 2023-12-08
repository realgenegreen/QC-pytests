import pytest
from requests import Response
import allure
from src.charset import charset
from src.api import Qual_api
from src.checks import Check

@allure.parent_suite('Authorisation')
@allure.suite('Register/Login jobs')
@allure.testcase('https://app.qase.io/project/QUAL?case=2', 'QUAL-2')
class Test_api():

    @allure.description('[API][Auth][Positive] Test for create, check and delete user')
    @pytest.mark.parametrize('username', [charset(6)])
    @pytest.mark.parametrize('password', [charset(20, True, True)])
    @allure.title('Requests')
    def test_requests(self, username, password):
        '''Collection of requests'''

        allure.dynamic.parameter('username', username)
        allure.dynamic.parameter('password', password)
#       Register
        with allure.step('User registration'):
            print('\nPOST method - new user registration')
            register_post: Response = Qual_api.register(username, password)
            print(f'{register_post.text}')
            Check.status_code(register_post, 200)
            Check.expected_keys(register_post, Qual_api.positive_keys(register=True))

            uid = register_post.json()['id']

#       Login
        with allure.step('Login of new user'):
            print('\nPOST method - login previously added user')
            login_post: Response = Qual_api.login(username, password)
            cookie = login_post.cookies.get_dict()
            print(f'{login_post.text}')
            Check.status_code(login_post, 200)
            Check.expected_keys(login_post, Qual_api.positive_keys(login=True))
            Check.expected_word(login_post, Qual_api.positive_keys(login=True)[0], 'Welcome')

#       Whoami check
        with allure.step('Confirm login'):
            print('\nGET method - login check')
            whoami_get: Response = Qual_api.get(cookie=cookie)
            print(f'{whoami_get.text}')
            Check.status_code(whoami_get, 200)
            Check.expected_keys(whoami_get, Qual_api.positive_keys(whoami=True))

#       Logout
        with allure.step('Log out user'):
            print('\nPOST method - logout')
            logout_post: Response = Qual_api.logout(cookie=cookie)
            print(f'{logout_post.text}')
            Check.status_code(logout_post, 200)
            Check.expected_keys(logout_post, Qual_api.positive_keys(logout=True))
            Check.expected_word(logout_post, Qual_api.positive_keys(logout=True)[0], 'out')

#       Login for delete
        with allure.step('Logining user for delete'):
            print('\nPOST method - login again for delete')
            login_post: Response = Qual_api.login(username, password)
            print(f'{login_post.text}')
            Check.status_code(login_post, 200)
            Check.expected_word(login_post, Qual_api.positive_keys(login=True)[0], 'Welcome')

        with allure.step('Delete user'):
            print('\nDELETE method')
            delete_delete: Response = Qual_api.delete(uid, cookie)
            print(f'{delete_delete.text}')
            Check.status_code(delete_delete, 200)
            Check.expected_keys(delete_delete, Qual_api.positive_keys(delete=True))
            Check.expected_word(delete_delete, Qual_api.positive_keys(delete=True)[0], 'Deleted')

#       Failed login & whoami
        with allure.step('Checking the delete success by login'):
            print('\nPOST method - login again to check fail')
            login_post: Response = Qual_api.login(username, password)
            print(f'{login_post.text}')
            Check.status_code(login_post, 401)
            Check.expected_word(login_post, Qual_api.negative_keys(login_post.status_code, login=True)[0], 'Incorrect')

        with allure.step('Checking the delete success by whoami'):
            print('\nGET method - failed check of login')
            whoami_get: Response = Qual_api.get(cookie=cookie)
            print(f'{whoami_get.text}')
            Check.status_code(whoami_get, 401)
            Check.expected_word(whoami_get, Qual_api.negative_keys(whoami_get.status_code, login=True)[0], 'not')

        print('\n-=ALL TESTS SUCCESSFULLY PASSED=-\n')
