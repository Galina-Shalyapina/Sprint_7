import pytest
import allure
from api_helpers import create_courier
from data import (
    register_new_courier_and_return_login_password,
    get_courier_data,
    Response
)


class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier):
        with allure.step("Регистрация нового курьера"):
            courier_data = register_new_courier_and_return_login_password()

        with allure.step("Проверка, что курьер создан успешно"):
            assert courier_data, "Не удалось создать курьера"
            assert "login" in courier_data, "Логин отсутствует в ответе"
            assert "password" in courier_data, "Пароль отсутствует в ответе"
            assert "first_name" in courier_data, "Имя отсутствует в ответе"
            assert "id" in courier_data, "ID курьера отсутствует в ответе"

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        with allure.step("Регистрация первого курьера"):
            first_courier = register_new_courier_and_return_login_password()
            assert first_courier, "Не удалось создать первого курьера"

        with allure.step("Попытка создать второго курьера с теми же данными"):
            payload = {
                "login": first_courier["login"],
                "password": first_courier["password"],
                "firstName": first_courier["first_name"],
            }
            response = create_courier(payload)

        with allure.step("Проверка кода ответа"):
            assert (
                response.status_code == 409
            ), f"Ожидался код 409, получен {response.status_code}"
        with allure.step("Проверка тела ответа"):
            assert response.json() == Response.DUPLICATE_COURIER

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка при отсутствии обязательного поля")
    def test_create_courier_missing_field(self, missing_field):
        with allure.step(f"Создание данных с отсутствующим полем: {missing_field}"):
            incomplete_data = get_courier_data()
            del incomplete_data[missing_field]
        with allure.step("Отправка запроса на создание курьера"):
            response = create_courier(incomplete_data)

        with allure.step("Проверка кода ответа"):
            assert (
                response.status_code == 400
            ), f"Ожидался код 400, получен {response.status_code}"

        with allure.step("Проверка тела ответа"):
            assert response.json() == Response.MISSING_CREATE_COURIER_FIELD
