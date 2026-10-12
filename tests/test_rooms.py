"""Тесты класса Room и функций работы с залами."""

from models import Room
from models.rooms import (
    add_room,
    check_room_capacity,
    find_room,
    sort_rooms,
)


def test_room_creation():
    room = Room(1, "Лофт", "LightBox", 10, 2500)
    assert room.id == 1
    assert room.name == "Лофт"
    assert room.capacity == 10


def test_room_is_suitable_for():
    room = Room(1, "Лофт", "LightBox", 10, 2500)
    assert room.is_suitable_for(5) is True
    assert room.is_suitable_for(15) is False


def test_room_str():
    room = Room(1, "Лофт", "LightBox", 10, 2500)
    assert "Лофт" in str(room)


def test_add_room():
    rooms = []
    room = add_room(rooms, "Лофт", "LightBox", 10, 2500)
    assert len(rooms) == 1
    assert room.id == 1


def test_find_room():
    rooms = []
    add_room(rooms, "Лофт", "LightBox", 10, 2500)
    found = find_room(rooms, "лофт")
    assert len(found) == 1


def test_check_room_capacity():
    rooms = []
    add_room(rooms, "Лофт", "LightBox", 10, 2500)
    assert check_room_capacity(rooms, 1, 5) is True
    assert check_room_capacity(rooms, 1, 20) is False


def test_sort_rooms():
    rooms = []
    add_room(rooms, "Лофт", "LightBox", 10, 2500)
    add_room(rooms, "Минимализм", "LightBox", 6, 1800)
    sorted_rooms = sort_rooms(rooms)
    assert sorted_rooms[0].price_per_hour == 1800
