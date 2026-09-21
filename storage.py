"""Модуль сохранения и загрузки данных в JSON."""

import json
import os
from typing import Any


def load_rooms(filename: str) -> dict[int, dict[str, Any]]:
    """Загрузить залы из JSON. При ошибке вернуть пустой словарь."""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {int(k): v for k, v in data.items()}
    except (json.JSONDecodeError, ValueError):
        return {}


def save_rooms(filename: str, rooms: dict[int, dict]) -> None:
    """Сохранить залы в JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(rooms, f, ensure_ascii=False, indent=2)


def load_bookings(filename: str) -> list[dict]:
    """Загрузить бронирования из JSON."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_bookings(filename: str, bookings: list[dict]) -> None:
    """Сохранить бронирования в JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=2)
