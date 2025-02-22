import requests
import random
import string
import allure

from api_helpers import create_courier, login_courier

VALID_ORDER = {
    "firstName": "Customer",
    "lastName": "Test",
    "address": "Test Street 123",
    "metroStation": "1",
    "phone": "+79991234567",
    "rentTime": 1,
    "deliveryDate": "2023-12-31",
    "comment": "Test order",
    "color": [],
}


def get_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {"login": login, "password": password, "firstName": first_name}


def register_new_courier_and_return_login_password():
    with allure.step("Генерация случайных данных для курьера"):
        payload = get_courier_data()
    with allure.step("Отправка запроса на регистрацию курьера"):
        response = create_courier(payload)

    if response.status_code == 201:
        with allure.step("Регистрация успешна, выполнение логина для получения ID"):
            login_payload = {"login": payload["login"], "password": payload["password"]}
            login_response = login_courier(login_payload)
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                return {
                    "login": payload["login"],
                    "password": payload["password"],
                    "first_name": payload["firstName"],
                    "id": courier_id,
                }
            else:
                return {}
    else:
        return {}
