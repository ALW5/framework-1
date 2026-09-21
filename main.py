"""Точка запуска приложения «Сервис управления фотостудией»."""


from pathlib import Path

from bookings import (
    cancel_booking,
    create_booking,
    get_booking_status,
    is_room_available,
)
from storage import (
    load_bookings,
    load_rooms,
    save_bookings,
    save_rooms,
)
from studios import (
    check_room_capacity,
    filter_rooms_by_capacity,
    find_room,
    sort_rooms,
)
from utils import input_date, input_int

DATA_DIR = Path("data")
ROOMS_FILE = DATA_DIR / "studios.json"
BOOKINGS_FILE = DATA_DIR / "bookings.json"


def show_rooms(rooms: dict[int, dict]) -> None:
    """Вывести список залов."""
    if not rooms:
        print("Залы не найдены.")
        return
    print(f"\n{'ID':<4}{'Название':<25}{'Студия':<20}{'Мест':<8}{'Цена/час':<10}")
    print("-" * 70)
    for room_id, room in rooms.items():
        print(
            f"{room_id:<4}{room['name']:<25}{room['studio']:<20}"
            f"{room['capacity']:<8}{room['price_per_hour']:<10}"
        )


def show_bookings(bookings: list[dict], rooms: dict[int, dict]) -> None:
    """Вывести список бронирований."""
    if not bookings:
        print("Бронирований нет.")
        return
    print(f"\n{'ID':<4}{'Зал':<25}{'Дата':<15}")
    print("-" * 50)
    for b in bookings:
        room_name = rooms.get(b["room_id"], {}).get("name", "—")
        print(f"{b['id']:<4}{room_name:<25}{b['date']:<15}")


def main() -> None:
    """Точка входа: цикл меню приложения."""
    DATA_DIR.mkdir(exist_ok=True)
    rooms = load_rooms(str(ROOMS_FILE))
    bookings = load_bookings(str(BOOKINGS_FILE))

    while True:
        print("\n=== Сервис управления фотостудией ===")
        print("1. Показать залы")
        print("2. Найти зал по названию")
        print("3. Проверить вместимость")
        print("4. Отобрать залы по вместимости")
        print("5. Сортировать залы по цене")
        print("6. Проверить доступность на дату")
        print("7. Забронировать зал")
        print("8. Отменить бронирование")
        print("9. Показать бронирования")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                show_rooms(rooms)
            elif choice == "2":
                query = input("Подстрока названия: ")
                ids = find_room(rooms, query)
                if ids:
                    print("Найдены залы:", ids)
                else:
                    print("Ничего не найдено.")
            elif choice == "3":
                room_id = input_int("ID зала: ")
                min_cap = input_int("Минимальная вместимость: ")
                print(check_room_capacity(rooms, room_id, min_cap))
            elif choice == "4":
                min_cap = input_int("Минимальная вместимость: ")
                print("Подходящие залы:", filter_rooms_by_capacity(rooms, min_cap))
            elif choice == "5":
                for room_id, room in sort_rooms(rooms):
                    print(f"{room_id}: {room['name']} — {room['price_per_hour']} руб/час")
            elif choice == "6":
                room_id = input_int("ID зала: ")
                bdate = input_date("Дата (ДД.ММ.ГГГГ): ")
                available = is_room_available(bookings, room_id, bdate)
                print(get_booking_status(available))
            elif choice == "7":
                room_id = input_int("ID зала: ")
                bdate = input_date("Дата (ДД.ММ.ГГГГ): ")
                booking = create_booking(bookings, room_id, bdate)
                if booking:
                    save_bookings(str(BOOKINGS_FILE), bookings)
                    print(f"Бронирование создано: id={booking['id']}")
                else:
                    print("Зал уже занят на эту дату.")
            elif choice == "8":
                booking_id = input_int("ID бронирования: ")
                if cancel_booking(bookings, booking_id):
                    save_bookings(str(BOOKINGS_FILE), bookings)
                    print("Бронирование отменено.")
                else:
                    print("Бронирование не найдено.")
            elif choice == "9":
                show_bookings(bookings, rooms)
            elif choice == "0":
                save_rooms(str(ROOMS_FILE), rooms)
                save_bookings(str(BOOKINGS_FILE), bookings)
                print("Данные сохранены. Выход.")
                break
            else:
                print("Неверный пункт меню.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
