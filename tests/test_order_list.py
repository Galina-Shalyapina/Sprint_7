import allure
from api_helpers import get_order_list


class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        with allure.step("Отправка запроса на получение списка заказов"):
            response = get_order_list()
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка, что orders является списком"):
            assert isinstance(response.json().get("orders"), list)
