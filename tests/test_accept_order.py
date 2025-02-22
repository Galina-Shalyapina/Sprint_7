import allure
from api_helpers import create_order, accept_order, get_order_by_number
from data import VALID_ORDER

class TestAcceptOrder:
    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, courier):
        with allure.step("Создание заказа"):
            order_response = create_order(VALID_ORDER)
            order_track = order_response.json()["track"]
        with allure.step("Получаем заказ по его номеру"):
            order = get_order_by_number(order_track)
            order_id = order.json()["order"]["id"]
        with allure.step(f"Отправка запроса на принятие заказа {order_id} курьером {courier['id']}"):
            response = accept_order(order_id, courier["id"])
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка тела ответа"):
            assert response.json() == {"ok": True}

    @allure.title("Ошибка при отсутствии courierId")
    def test_accept_order_no_courier_id(self):
        with allure.step("Отправка запроса на принятие заказа без courierId"):
            response = accept_order("1", "")  # Пустой courierId
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400
