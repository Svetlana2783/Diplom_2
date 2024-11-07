class User:
    data_correct = {
        "email": 'test@list.ru',
        "password": "Test123+"
    }

    data_negative = {
        "email": 'testt@list.ru',
        "password": "Test123+"
    }

    data_double = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": "Светлана"
    }

    data_without_email = {
        "email": '',
        "password": "Test123+",
        "name": "Светлана"
    }

    data_without_password = {
        "email": 'test@list.ru',
        "password": "",
        "name": "Светлана"
    }

    data_without_name = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": ""
    }

    data_updated = {
        "email": 'test@list.ru',
        "password": "Test123+",
        "name": "Svetlana"
    }
