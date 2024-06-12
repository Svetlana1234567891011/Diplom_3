import random
import string

import requests
import allure
from utils.urls import URLS


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


class BaseRequests:
    host = URLS.MAIN_PAGE_URL

    def post_request_transform_token(self, url, data, token):
        headers = {'authorization': token}
        response = requests.post(url=url, data=data, headers=headers)
        # if response.headers.get('Content-Type') and 'application/json' in response.headers['Content-Type']:
        return response.json()

    def post_request_transform(self, url, data):
        response = requests.post(url=url, json=data)
        if response.headers.get('Content-Type') and 'application/json' in response.headers['Content-Type']:
            # if 'application/json' in response.headers['Content-Type']:
            #     return response.json()
            # else:
            #     return response.text
            # return {"status_code": response.status_code, "text": response.json()}
            return response.json()
        else:
            return {"status_code": response.status_code, "text": response.text}

    # def exec_delete_request(self, url, token):
    #     headers = {"Content-Type": "application/json", 'authorization': token}
    #     response = requests.delete(url=url, headers=headers)
    #     if 'application/json' in response.headers['Content-Type']:
    #         return response.json()
    #     else:
    #         return response.text


class UserRequests(BaseRequests):
    user_handler = 'api/auth/register'
    manipulate_user_handler = 'api/auth/user'

    # @allure.step('Создаем пользователя, отправив запрос POST')
    # def post_create_user(self, data):
    #     url = f"{self.host}{self.user_handler}"
    #     response = requests.post(url, data=data)
    #     return response
    @allure.step('Создаем пользователя, отправив запрос POST')
    def post_create_courier(self, data=None):
        url = f"{self.host}{self.user_handler}"
        return self.post_request_transform(url, data=data)

    @allure.step('Удаляем пользователя, отправив запрос DELETE')
    def delete_user(self, token=None):
        headers = {"Content-Type": "application/json", 'authorization': token}
        url = f"{self.host}{self.manipulate_user_handler}"
        response = requests.delete(url=url, headers=headers)
        return response
