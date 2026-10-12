"""Модель зала фотостудии и функции работы с залами."""

from typing import List, Optional


class Room:
    """Зал фотостудии, доступный для бронирования."""

    def __init__(
        self,
        room_id: int,
        name: str,
        studio: str,
        capacity: int,
        price_per_hour: float,
    ) -> None:
        """Создать объект зала."""
        self.id = room_id
        self.name = name
        self.studio = studio
        self.capacity = capacity
        self.price_per_hour = price_per_hour

    def is_suitable_for(self, people_count: int) -> bool:
        """Проверить, подходит ли зал по вместимости."""
        return self.capacity >= people_count

    def __str__(self) -> str:
        """Вернуть строковое представление зала."""
        return (
            f"Зал «{self.name}» ({self.studio}), "
            f"{self.capacity} мест, {self.price_per_hour} руб/час"
        )


def add_room(
    rooms: List[Room],
    name: str,
    studio: str,
    capacity: int,
    price_per_hour: float,
) -> Room:
    """Создать объект Room и добавить его в коллекцию."""
    new_id = max((r.id for r in rooms), default=0) + 1
    room = Room(new_id, name, studio, capacity, price_per_hour)
    rooms.append(room)
    return room


def find_room(rooms: List[Room], query: str) -> List[Room]:
    """Найти залы по подстроке названия."""
    query_lower = query.lower()
    return [r for r in rooms if query_lower in r.name.lower()]


def check_room_capacity(
    rooms: List[Room], room_id: int, min_capacity: int
) -> bool:
    """Проверить вместимость зала с указанным id."""
    for room in rooms:
        if room.id == room_id:
            return room.is_suitable_for(min_capacity)
    return False


def filter_rooms_by_capacity(
    rooms: List[Room], min_capacity: int
) -> List[Room]:
    """Отобрать залы по вместимости."""
    return [r for r in rooms if r.is_suitable_for(min_capacity)]


def sort_rooms(rooms: List[Room]) -> List[Room]:
    """Отсортировать залы по цене за час."""
    return sorted(rooms, key=lambda r: r.price_per_hour)


def find_room_by_id(rooms: List[Room], room_id: int) -> Optional[Room]:
    """Найти зал по id. Вернуть объект или None."""
    for room in rooms:
        if room.id == room_id:
            return room
    return None
