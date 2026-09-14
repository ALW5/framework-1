"""
Сервис управления фотостудией.
Начальный сценарий (ПР1).
Реализованы функции: информация о студии, проверка доступности зала,
расчёт стоимости бронирования, определение статуса клиента.
"""

from datetime import date


def get_studio_info(studio_name, address, rooms_count):
    """Возвращает информацию о фотостудии."""
    return (
        f"Студия: {studio_name}\n"
        f"Адрес: {address}\n"
        f"Количество залов: {rooms_count}"
    )


def check_room_availability(is_available):
    """Проверяет доступность зала на выбранную дату."""
    if is_available:
        return "Зал свободен — можно бронировать"
    return "Зал занят — выберите другое время"


def calculate_booking_cost(hours, price_per_hour, is_discount):
    """Рассчитывает стоимость бронирования.
    
    is_discount — True, если у клиента скидка 10%.
    """
    total = hours * price_per_hour
    if is_discount:
        total = total * 0.9
    return total


def get_client_status(client_type):
    """Определяет статус клиента по типу."""
    if client_type == "vip":
        return "VIP-клиент — персональный менеджер"
    elif client_type == "regular":
        return "Постоянный клиент — скидка 10%"
    else:
        return "Новый клиент — добро пожаловать!"


# --- Демонстрация работы сценария ---

studio_name = "LightBox Studio"
studio_address = "г. Москва, ул. Пушкина, 10"
rooms_count = 4

room_name = "Зал «Лофт»"
room_capacity = 10
booking_date = date(2026, 9, 20)
is_available = True

client_name = "Иван Петров"
client_type = "regular"
hours = 3
price_per_hour = 2500
is_discount = True

print(get_studio_info(studio_name, studio_address, rooms_count))
print("---")
print(f"Зал: {room_name}")
print(f"Вместимость: {room_capacity} человек")
print(f"Дата бронирования: {booking_date}")
print(check_room_availability(is_available))
print("---")
print(f"Клиент: {client_name}")
print(f"Статус: {get_client_status(client_type)}")
cost = calculate_booking_cost(hours, price_per_hour, is_discount)
print(f"Стоимость бронирования: {cost:.2f} руб.")