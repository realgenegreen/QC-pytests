import allure
import requests
from src.logger import Logger

class Http_methods:
    headers={
            'accept':'application/json',
            'Content-Type':'application/json'
            }

    @staticmethod
    def get(url, cookie=False):
        with allure.step('GET'):
            Logger.add_request(url, method='GET')
            if cookie:
                result = requests.get(url, headers=Http_methods.headers, cookies=cookie, timeout=50)
            else:
                result = requests.get(url, headers=Http_methods.headers, cookies='', timeout=50)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body, form=False, cookie=False):
        with allure.step('POST'):
            Logger.add_request(url, method='POST')
            if form and cookie:
                result = requests.post(url, json=body, headers=form, cookies=cookie, timeout=50)
            elif form:
                result = requests.post(url, json=body, headers=form, cookies='', timeout=50)
            elif cookie:
                result = requests.post(url, json=body, headers='', cookies=cookie, timeout=50)
            else:
                result = requests.post(url, json=body, headers=Http_methods.headers, cookies='', timeout=50)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('PUT'):
            Logger.add_request(url, method='PUT')
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies='', timeout=50)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, cookies):
        with allure.step('DELETE'):
            Logger.add_request(url, method='DELETE')
            result = requests.delete(url, json='', headers=Http_methods.headers, cookies=cookies, timeout=50)
            Logger.add_response(result)
            return result
