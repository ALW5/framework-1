"""Модуль работы с бронированиями."""

from datetime import date


def get_booking_status(is_available: bool) -> str:
    """Вернуть текстовый статус зала. Функция перенесена из ПР1."""
    if is_available:
        return "Зал доступен для бронирования"
    return "Зал уже занят"


def is_room_available(
    bookings: list[dict], room_id: int, booking_date: date
) -> bool:
    """Проверить, свободен ли зал на дату."""
    date_str = booking_date.isoformat()
    for booking in bookings:
        if booking["room_id"] == room_id and booking["date"] == date_str:
            return False
    return True


def create_booking(
    bookings: list[dict], room_id: int, booking_date: date
) -> dict | None:
    """Создать бронирование, если зал свободен."""
    if not is_room_available(bookings, room_id, booking_date):
        return None
    new_id = max((b["id"] for b in bookings), default=0) + 1
    booking = {
        "id": new_id,
        "room_id": room_id,
        "date": booking_date.isoformat(),
    }
    bookings.append(booking)
    return booking


def cancel_booking(bookings: list[dict], booking_id: int) -> bool:
    """Отменить бронирование по id. Возвращает True при успехе."""
    for i, booking in enumerate(bookings):
        if booking["id"] == booking_id:
            bookings.pop(i)
            return True
    return False
