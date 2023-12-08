'''Methods collection for api checks'''
import json
import allure
from requests import Response

class Check():
    '''Class'''
    @staticmethod
    def status_code(response: Response, status_code):
        '''Method that compares given status with returned status'''
        with allure.step('Compare given status with returned status'):
            assert status_code == response.status_code
            if response.status_code == status_code:
                print(f'Correct status code: {str(response.status_code)}')
            else:
                print(f'Wrong status code: {str(response.status_code)}')

    @staticmethod
    def expected_keys(response: Response, key):
        '''Method that checks expected keys in response'''
        with allure.step('Check expected keys in response'):
            x = json.loads(response.text)
            assert list(x) == key
            print('Correct keys')

    @staticmethod
    def expected_values(response: Response, key, value):
        '''Method that checks expected values in response'''
        with allure.step('Check expected values in response'):
            check = response.json().get(key)
            assert check == value
            print(f'Value of <{key}> is correct')

    @staticmethod
    def expected_word(response: Response, key, word):
        '''Method that checks presense of the given word in response'''
        with allure.step('Check presense of the given word in response'):
            check = response.json().get(key)
            if word in check:
                print(f'<{word}> is present in value')
            else:
                print(f'There is no <{word}> in value')
