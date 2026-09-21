"""Вспомогательные функции безопасного ввода."""

from datetime import date


def input_int(prompt: str) -> int:
    """Запросить целое число. Повторять при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str) -> date:
    """Запросить дату в формате ДД.ММ.ГГГГ. Повторять при ошибке."""
    while True:
        try:
            raw = input(prompt)
            day, month, year = map(int, raw.split("."))
            return date(year, month, day)
        except (ValueError, TypeError):
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ.")
