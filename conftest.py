import pytest
from api_helpers import delete_courier
from data import register_new_courier_and_return_login_password

@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()
    if not courier_data:
        pytest.fail("Не удалось создать курьера")
    yield courier_data
    # Очистка: удаление курьера после теста
    if "id" in courier_data:
        delete_courier(courier_data["id"])