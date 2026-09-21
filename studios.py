"""Модуль работы с залами фотостудии."""

from typing import Any


def add_room(
    rooms: dict[int, dict[str, Any]],
    name: str,
    studio: str,
    capacity: int,
    price_per_hour: float,
) -> int:
    """Добавить зал в словарь rooms. Возвращает id нового зала."""
    new_id = max(rooms.keys(), default=0) + 1
    rooms[new_id] = {
        "name": name,
        "studio": studio,
        "capacity": capacity,
        "price_per_hour": price_per_hour,
    }
    return new_id


def find_room(rooms: dict[int, dict], query: str) -> list[int]:
    """Найти залы по подстроке названия. Возвращает список id."""
    query_lower = query.lower()
    return [
        room_id
        for room_id, room in rooms.items()
        if query_lower in room["name"].lower()
    ]


def check_room_capacity(
    rooms: dict[int, dict], room_id: int, min_capacity: int
) -> bool:
    """Вернуть True, если вместимость зала не меньше min_capacity."""
    if room_id not in rooms:
        return False
    return rooms[room_id]["capacity"] >= min_capacity


def filter_rooms_by_capacity(
    rooms: dict[int, dict], min_capacity: int
) -> list[int]:
    """Отобрать залы по вместимости (генератор)."""
    return [
        room_id
        for room_id, room in rooms.items()
        if room["capacity"] >= min_capacity
    ]


def sort_rooms(rooms: dict[int, dict]) -> list[tuple[int, dict]]:
    """Отсортировать залы по цене за час (lambda)."""
    return sorted(
        rooms.items(),
        key=lambda item: item[1]["price_per_hour"],
    )
