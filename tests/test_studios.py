"""Тесты для модуля studios."""

from studios import add_room, check_room_capacity, find_room


def test_add_room():
    rooms = {}
    add_room(rooms, "Зал Лофт", "LightBox", 10, 2500)
    assert len(rooms) == 1


def test_find_room():
    rooms = {}
    add_room(rooms, "Зал Лофт", "LightBox", 10, 2500)
    assert find_room(rooms, "лофт") == [1]


def test_check_room_capacity_true():
    rooms = {}
    add_room(rooms, "Зал Лофт", "LightBox", 10, 2500)
    assert check_room_capacity(rooms, 1, 5) is True


def test_check_room_capacity_false():
    rooms = {}
    add_room(rooms, "Зал Лофт", "LightBox", 10, 2500)
    assert check_room_capacity(rooms, 1, 20) is False
