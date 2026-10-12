"""Точка запуска приложения «Сервис управления фотостудией»."""

from pathlib import Path
from typing import List

from models import Booking, Client, Room
from models.bookings import (
    cancel_booking,
    create_booking,
    get_booking_status,
    is_room_available,
)
from models.clients import find_client_by_id
from models.rooms import (
    check_room_capacity,
    find_room,
    find_room_by_id,
    sort_rooms,
)
from storage import (
    load_bookings,
    load_clients,
    load_rooms,
    save_bookings,
    save_clients,
    save_rooms,
)
from utils import input_date, input_int

DATA_DIR = Path("data")
ROOMS_FILE = DATA_DIR / "rooms.json"
CLIENTS_FILE = DATA_DIR / "clients.json"
BOOKINGS_FILE = DATA_DIR / "bookings.json"


def show_rooms(rooms: List[Room]) -> None:
    """Вывести список залов."""
    if not rooms:
        print("Залы не найдены.")
        return
    for room in rooms:
        print(room)


def show_clients(clients: List[Client]) -> None:
    """Вывести список клиентов."""
    if not clients:
        print("Клиенты не найдены.")
        return
    for client in clients:
        print(client)


def show_bookings(bookings: List[Booking]) -> None:
    """Вывести список броней."""
    if not bookings:
        print("Бронирований нет.")
        return
    for booking in bookings:
        print(booking)


def create_new_booking(
    bookings: List[Booking],
    rooms: List[Room],
    clients: List[Client],
) -> None:
    """Сценарий создания бронирования."""
    room_id = input_int("ID зала: ")
    room = find_room_by_id(rooms, room_id)
    if room is None:
        print("Зал не найден.")
        return

    client_id = input_int("ID клиента: ")
    client = find_client_by_id(clients, client_id)
    if client is None:
        print("Клиент не найден.")
        return

    booking_date = input_date("Дата (ДД.ММ.ГГГГ): ").isoformat()
    booking = create_booking(bookings, room, booking_date, client)
    if booking is None:
        print("Зал уже занят на эту дату.")
    else:
        print(f"Бронирование создано: {booking}")


def main() -> None:
    """Точка входа приложения."""
    DATA_DIR.mkdir(exist_ok=True)
    rooms = load_rooms(str(ROOMS_FILE))
    clients = load_clients(str(CLIENTS_FILE))
    bookings = load_bookings(str(BOOKINGS_FILE), rooms, clients)

    while True:
        print("\n=== Сервис управления фотостудией ===")
        print("1. Показать залы")
        print("2. Найти зал")
        print("3. Проверить вместимость")
        print("4. Сортировать залы по цене")
        print("5. Показать клиентов")
        print("6. Проверить доступность зала на дату")
        print("7. Создать бронирование")
        print("8. Отменить бронирование")
        print("9. Показать бронирования")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                show_rooms(rooms)
            elif choice == "2":
                query = input("Подстрока названия: ")
                for r in find_room(rooms, query):
                    print(r)
            elif choice == "3":
                room_id = input_int("ID зала: ")
                min_cap = input_int("Минимальная вместимость: ")
                print(check_room_capacity(rooms, room_id, min_cap))
            elif choice == "4":
                for r in sort_rooms(rooms):
                    print(r)
            elif choice == "5":
                show_clients(clients)
            elif choice == "6":
                room_id = input_int("ID зала: ")
                room = find_room_by_id(rooms, room_id)
                if room is None:
                    print("Зал не найден.")
                    continue
                d = input_date("Дата (ДД.ММ.ГГГГ): ").isoformat()
                available = is_room_available(bookings, room, d)
                print(get_booking_status(available))
            elif choice == "7":
                create_new_booking(bookings, rooms, clients)
            elif choice == "8":
                booking_id = input_int("ID брони: ")
                if cancel_booking(bookings, booking_id):
                    print("Бронирование отменено.")
                else:
                    print("Бронирование не найдено.")
            elif choice == "9":
                show_bookings(bookings)
            elif choice == "0":
                save_rooms(str(ROOMS_FILE), rooms)
                save_clients(str(CLIENTS_FILE), clients)
                save_bookings(str(BOOKINGS_FILE), bookings)
                print("Данные сохранены. Выход.")
                break
            else:
                print("Неверный пункт меню.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
    