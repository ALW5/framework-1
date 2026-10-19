# Сервис управления фотостудией

## Назначение

Приложение для управления залами фотостудии и бронированиями.
Консольная версия (ПР3) дополнена веб-интерфейсом на Django (ПР5).

## Используемые технологии

- Python 3
- Django 5.2 — веб-фреймворк
- HTML, CSS, Bootstrap 5.3
- pytest — тесты
- flake8 — проверка кода

## Страницы веб-интерфейса

| URL | Назначение | View |
|-----|-----------|------|
| `/` | главная | `homepage.views.index` |
| `/rooms/` | список залов | `rooms.views.rooms` |
| `/rooms/<int:room_id>/` | карточка зала | `rooms.views.room_detail` |
| `/bookings/` | список броней | `bookings.views.bookings` |
| `/bookings/<int:booking_id>/` | карточка брони | `bookings.views.booking_detail` |

## Структура проекта
project/
├── manage.py
├── main.py # консольная версия (сохранена)
├── storage.py
├── utils.py
├── roomly/ # настройки Django-проекта
├── homepage/ # приложение главной страницы
├── rooms/ # приложение залов
├── bookings/ # приложение броней
├── models/ # классы ПР3 (Room, Client, Booking)
├── data/ # JSON-данные
└── tests/ # pytest
 
## Запуск

### Веб-версия
```bash
python manage.py migrate
python manage.py runserve
