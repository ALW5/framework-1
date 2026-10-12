"""Тесты класса Booking и функций бронирования."""

from models import Booking, Client, Room
from models.bookings import (
    cancel_booking,
    create_booking,
    is_room_available,
)


def _make_room():
    return Room(1, "Лофт", "LightBox", 10, 2500)


def _make_client():
    return Client(1, "Иван", "ivan@example.com", "+79990001122")


def test_booking_creation():
    room = _make_room()
    client = _make_client()
    booking = Booking(1, room, "2026-09-20", client)
    assert booking.id == 1
    assert booking.room is room
    assert booking.client is client
    assert booking.is_cancelled is False


def test_booking_cancel():
    booking = Booking(1, _make_room(), "2026-09-20", _make_client())
    booking.cancel()
    assert booking.is_cancelled is True


def test_room_available_empty():
    bookings = []
    assert is_room_available(bookings, _make_room(), "2026-09-20") is True


def test_duplicate_booking_forbidden():
    bookings = []
    room = _make_room()
    client = _make_client()
    create_booking(bookings, room, "2026-09-20", client)
    assert is_room_available(bookings, room, "2026-09-20") is False


def test_cancelled_booking_does_not_block():
    bookings = []
    room = _make_room()
    client = _make_client()
    booking = create_booking(bookings, room, "2026-09-20", client)
    booking.cancel()
    assert is_room_available(bookings, room, "2026-09-20") is True


def test_cancel_booking():
    bookings = []
    room = _make_room()
    client = _make_client()
    create_booking(bookings, room, "2026-09-20", client)
    assert cancel_booking(bookings, 1) is True
    assert bookings[0].is_cancelled is True
