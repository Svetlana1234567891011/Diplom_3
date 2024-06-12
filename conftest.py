import pytest
import allure
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from utils.special_requests import UserRequests
import string
import random

fake = Faker()


@allure.step('Открываем браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == 'firefox':
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    yield driver
    driver.quit()


@pytest.fixture()
@allure.step('Создаем случайную строку')
def generate_random_string_fix():
    def _generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string  # Возвращаем сгенерированную строку

    return _generate_random_string


@pytest.fixture()
@allure.step('Создаем случайную строку длиной 10 символов')
def generate_random_string_10(generate_random_string_fix):
    randoms_string = generate_random_string_fix(10)
    return randoms_string


@allure.step('payload для пользователя')
@pytest.fixture(scope='function', autouse=True)
def create_payload(generate_random_string_10):
    name = generate_random_string_10
    password = generate_random_string_10
    email = fake.email()

    payload = {
        "name": name,
        "password": password,
        "email": email
    }

    return payload


created_users_list = []


@pytest.fixture(scope='function')
def user_with_payload(create_payload):
    user_requests = UserRequests()
    # Создаем пользователя
    payload = create_payload
    user_requests.payload = payload  # Добавляем payload в объект
    response_new = user_requests.post_create_courier(data=payload)
    access_token = response_new.get('accessToken')
    created_users_list.append(user_requests)
    if access_token:
        user_requests.access_token = access_token
    return user_requests


@pytest.fixture(scope='function', autouse=True)
def cleanup_user():
    response = {}

    yield response
    if 'token' in response:
        UserRequests().delete_user(token=response['token'])
