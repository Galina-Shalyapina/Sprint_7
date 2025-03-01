import pytest
import allure
from api_helpers import login_courier
from data import Response


class TestCourierLogin:
    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, courier):
        with allure.step("Отправка запроса на логин курьера"):
            response = login_courier({"login": courier["login"], "password": courier["password"]})
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка наличия id в ответе"):
            assert "id" in response.json()

    @allure.title("Ошибка при неверном пароле")
    def test_login_courier_wrong_password(self, courier):
        with allure.step("Отправка запроса на логин с неверным паролем"):
            response = login_courier({"login": courier["login"], "password": "wrong"})
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 404
        with allure.step("Проверка тела ответа"):
            assert response.json() == Response.WRONG_LOGIN_OR_PASSWORD
