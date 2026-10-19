"""Сохранение и загрузка данных в JSON с преобразованием в объекты."""

import json
import os
from typing import List

from models import Booking, Client, Room


def load_rooms(filename: str) -> List[Room]:
    """Загрузить залы из JSON в виде списка объектов Room."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [
            Room(
                room_id=item["id"],
                name=item["name"],
                studio=item["studio"],
                capacity=item["capacity"],
                price_per_hour=item["price_per_hour"],
            )
            for item in data
        ]
    except (json.JSONDecodeError, KeyError, ValueError):
        return []


def save_rooms(filename: str, rooms: List[Room]) -> None:
    """Сохранить объекты Room в JSON."""
    data = [
        {
            "id": r.id,
            "name": r.name,
            "studio": r.studio,
            "capacity": r.capacity,
            "price_per_hour": r.price_per_hour,
        }
        for r in rooms
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_clients(filename: str) -> List[Client]:
    """Загрузить клиентов из JSON в виде списка объектов Client."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Client.from_data(item) for item in data]
    except (json.JSONDecodeError, KeyError, ValueError):
        return []


def save_clients(filename: str, clients: List[Client]) -> None:
    """Сохранить объекты Client в JSON."""
    data = [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone,
        }
        for c in clients
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_bookings(
    filename: str,
    rooms: List[Room],
    clients: List[Client],
) -> List[Booking]:
    """Загрузить брони, восстановив связи с Room и Client."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []

    bookings: List[Booking] = []
    for item in data:
        booking = Booking.from_data(item, rooms, clients)
        if booking is not None:
            bookings.append(booking)
    return bookings


def save_bookings(filename: str, bookings: List[Booking]) -> None:
    """Сохранить брони: объекты Room и Client → их id."""
    data = [
        {
            "id": b.id,
            "room_id": b.room.id,
            "booking_date": b.booking_date,
            "client_id": b.client.id,
            "is_cancelled": b.is_cancelled,
        }
        for b in bookings
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
