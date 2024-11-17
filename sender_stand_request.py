import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)


# Получение заказа по номеру трекера
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))
