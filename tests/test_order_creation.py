import pytest
import allure
from api_helpers import create_order
from data import VALID_ORDER


class TestOrderCreation:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Создание заказа с разными цветами")
    def test_create_order_with_colors(self, color):
        order_data = VALID_ORDER.copy()
        order_data["color"] = color
        with allure.step(f"Отправка запроса на создание заказа с цветом: {color}"):
            response = create_order(order_data)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201
        with allure.step("Проверка наличия track в ответе"):
            assert "track" in response.json()
