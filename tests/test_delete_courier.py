import allure
from api_helpers import delete_courier

class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self, courier):
        with allure.step("Отправка запроса на удаление курьера"):
            response = delete_courier(courier["id"])
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка тела ответа"):
            assert response.json() == {"ok": True}

    @allure.title("Ошибка при удалении без ID")
    def test_delete_courier_no_id(self):
        with allure.step("Отправка запроса на удаление без ID"):
            response = delete_courier("")  # Пустой ID
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 404
