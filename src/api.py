from urllib.parse import urlencode
from src.http_methods import Http_methods

base_url = 'http://localhost:5001'

class Qual_api():

    @staticmethod
    def register(username, password):
        url = base_url+'/register'
        json={
            "username": username,
            "password": password
            }
        register_post = Http_methods.post(url, json)
        print(f'\tusername:{username}\n\tpassword:{password}')
        return register_post

    @staticmethod
    def login(username, password):
        url = base_url+'/login'
        urlform = urlencode(dict(grant_type='',username=username,password=password,scope='',client_id='',client_secret=''))
        headers={
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
        login_post = Http_methods.post(url, urlform, form=headers)
        return login_post

    @staticmethod
    def get(cookie=False):
        url = base_url+'/users/whoami'
        if cookie:
            whoami_get = Http_methods.get(url, cookie=cookie)
        else:
            whoami_get = Http_methods.get(url)
        return whoami_get

    @staticmethod
    def logout(cookie=False):
        url = base_url+'/logout'
        json={}
        if cookie:
            logout_post = Http_methods.post(url, json, cookie=cookie)
        else:
            logout_post = Http_methods.post(url, json)
        return logout_post

    @staticmethod
    def delete(uid, cookie):
        url = base_url+'/user/'+str(uid)
        delete_post = Http_methods.delete(url, cookie)
        return delete_post

    @staticmethod
    def positive_keys(register=False, login=False, whoami=False, logout=False, delete=False):
        if register:
            return ['id', 'username', 'full_name']
        if login:
            return ['message']
        if whoami:
            return ['id', 'username', 'full_name']
        if logout:
            return ['message']
        if delete:
            return ['message']

    @staticmethod
    def negative_keys(status, register=False, login=False, whoami=False, logout=False, delete=False):
        if status == 401:
            if register:
                return ['detail']
            if login:
                return ['detail']
            if whoami:
                return ['detail']
            if logout:
                return ['detail']
            if delete:
                return ['detail']
        else:
            print('Some validation error: 422, 405, etc')
            return ['detail']
