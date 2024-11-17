#Войнаровская Элина 23-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

#Автотест
def test_get_order_info_by_track():
    track = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200