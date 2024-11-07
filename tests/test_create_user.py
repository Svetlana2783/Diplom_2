import pytest
import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User
from helpers.helpers import create_data_user

@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Создание уникального пользователя')
    @allure.title('Создание уникального пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description('При создании дублирующего пользователя возвращается предупреждение')
    @allure.title('Создание пользователя который уже есть в системе')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=User.data_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('При создании пользователя с некорректными данными возвращается предупреждение')
    @allure.title('Создание пользователя с некорректными данными/ с незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
