import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description('При авторизация под существующим пользователем происходит успешная авторизация')
    @allure.title('Авторизация под существующим пользователем')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('При авторизация под пользователем с некорректным логином/паролем, возвращается предупреждение')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
