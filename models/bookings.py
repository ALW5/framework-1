"""Модель бронирования и функции работы с бронированиями."""

from typing import List, Optional

from models.clients import Client, find_client_by_id
from models.rooms import Room, find_room_by_id


class Booking:
    """Бронирование зала клиентом."""

    def __init__(
        self,
        booking_id: int,
        room: Room,
        booking_date: str,
        client: Client,
    ) -> None:
        """Создать объект бронирования."""
        self.id = booking_id
        self.room = room
        self.booking_date = booking_date
        self.client = client
        self.is_cancelled = False

    def cancel(self) -> None:
        """Отменить бронирование."""
        self.is_cancelled = True

    def __str__(self) -> str:
        """Строковое представление с учётом статуса."""
        status = "ОТМЕНЕНО" if self.is_cancelled else "АКТИВНО"
        return (
            f"[{status}] Бронь #{self.id}: {self.room.name} "
            f"на {self.booking_date}, клиент: {self.client.name}"
        )

    @classmethod
    def from_data(
        cls,
        data: dict,
        rooms: List[Room],
        clients: List[Client],
    ) -> Optional["Booking"]:
        """Создать Booking из JSON, найдя связанные Room и Client."""
        room = find_room_by_id(rooms, data["room_id"])
        client = find_client_by_id(clients, data["client_id"])
        if room is None or client is None:
            return None
        booking = cls(
            booking_id=data["id"],
            room=room,
            booking_date=data["booking_date"],
            client=client,
        )
        booking.is_cancelled = data.get("is_cancelled", False)
        return booking


def is_room_available(
    bookings: List[Booking],
    room: Room,
    booking_date: str,
) -> bool:
    """Проверить, свободен ли зал на дату."""
    for booking in bookings:
        if booking.is_cancelled:
            continue
        if booking.room.id == room.id and booking.booking_date == booking_date:
            return False
    return True


def create_booking(
    bookings: List[Booking],
    room: Room,
    booking_date: str,
    client: Client,
) -> Optional[Booking]:
    """Создать бронирование, если зал свободен. Иначе вернуть None."""
    if not is_room_available(bookings, room, booking_date):
        return None
    new_id = max((b.id for b in bookings), default=0) + 1
    booking = Booking(new_id, room, booking_date, client)
    bookings.append(booking)
    return booking


def cancel_booking(bookings: List[Booking], booking_id: int) -> bool:
    """Найти бронь и вызвать её метод cancel()."""
    for booking in bookings:
        if booking.id == booking_id:
            booking.cancel()
            return True
    return False


def get_booking_status(is_available: bool) -> str:
    """Вернуть текстовый статус. Функция перенесена из ПР1."""
    if is_available:
        return "Зал доступен для бронирования"
    return "Зал уже занят"


def find_booking_by_id(
    bookings: List[Booking], booking_id: int
) -> Optional[Booking]:
    """Найти бронирование по идентификатору."""
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    return None
