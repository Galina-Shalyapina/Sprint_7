import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

def create_courier(data):
    return requests.post(f"{BASE_URL}/api/v1/courier", json=data)

def login_courier(data):
    return requests.post(f"{BASE_URL}/api/v1/courier/login", json=data)

def create_order(data):
    return requests.post(f"{BASE_URL}/api/v1/orders", json=data)

def get_order_list():
    return requests.get(f"{BASE_URL}/api/v1/orders")

def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")

def accept_order(order_id, courier_id):
    return requests.put(f"{BASE_URL}/api/v1/orders/accept/{order_id}?courierId={courier_id}")

def cancel_order(track_number):
    return requests.put(f"{BASE_URL}/api/v1/orders/cancel?track={track_number}")

def get_order_by_number(track_number):
    return requests.get(f"{BASE_URL}/api/v1/orders/track?t={track_number}")
