from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'test@list.ru',
        "password": "Test123+"}

    data_negative = {
        "email": 'testt@list.ru',
        "password": "Test123+"}

    data_double = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": "Светлана"}

    data_without_email = {
        "email": '',
        "password": "Test123+",
        "name": "Светлана"}

    data_without_password = {
        "email": 'test@list.ru',
        "password": "",
        "name": "Светлана"}

    data_without_name = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": ""}

    data_updated = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": "Svetlana"}
