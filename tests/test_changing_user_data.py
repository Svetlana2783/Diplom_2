import allure
import requests

from data.handlers import Urls, Handlers
from helpers.helpers import create_data_user
from tests.api_requests import change_user_data  # Импортируем метод из нового модуля

@allure.suite('Изменение данных пользователя')
class TestChangingUserData:

    @allure.description("При попытке сменить email у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, create_user):
        new_email = create_data_user()["email"]
        r = change_user_data(create_user, 'email', new_email)
        assert r.status_code == 200 and r.json()['user']['email'] == new_email

    @allure.description("При попытке сменить password у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, create_user):
        new_password = create_data_user()["password"]
        r = change_user_data(create_user, 'password', new_password)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("При попытке сменить name у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, create_user):
        new_name = create_data_user()["name"]
        r = change_user_data(create_user, 'name', new_name)
        assert r.status_code == 200 and r.json()['user']['name'] == new_name

    @allure.description("При попытке смены данных пользователя без авторизации, возвращается предупреждение")
    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_not_auth(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", data=create_data_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
