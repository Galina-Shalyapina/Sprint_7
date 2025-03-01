import allure
from api_helpers import create_order, get_order_by_number
from data import VALID_ORDER, Response


class TestGetOrder:
    @allure.title("Успешное получение заказа по номеру")
    def test_get_order_by_number_success(self):
        with allure.step("Создание заказа"):
            order_response = create_order(VALID_ORDER)
            track_number = order_response.json()["track"]
        with allure.step(f"Отправка запроса на получение заказа по номеру {track_number}"):
            response = get_order_by_number(track_number)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка наличия order в ответе"):
            assert "order" in response.json()

    @allure.title("Ошибка при отсутствии номера заказа")
    def test_get_order_no_track(self):
        with allure.step("Отправка запроса без номера заказа"):
            response = get_order_by_number("")
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка тела ответа"):
            assert response.json() == Response.MISSING_PARAM
