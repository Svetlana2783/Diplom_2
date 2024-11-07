import requests
from data.handlers import Urls, Handlers

def change_user_data(create_user, field, value):
    payload = {field: value}
    token = {'Authorization': create_user[3]}
    r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
    return r
