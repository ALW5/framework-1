"""Тесты для модуля bookings."""

from datetime import date
from bookings import create_booking, is_room_available


def test_is_room_available_empty():
    bookings = []
    assert is_room_available(bookings, 1, date(2026, 9, 20)) is True


def test_duplicate_booking_forbidden():
    bookings = []
    create_booking(bookings, 1, date(2026, 9, 20))
    assert is_room_available(bookings, 1, date(2026, 9, 20)) is False


def test_create_booking_returns_dict():
    bookings = []
    booking = create_booking(bookings, 1, date(2026, 9, 20))
    assert booking is not None
    assert booking["room_id"] == 1
