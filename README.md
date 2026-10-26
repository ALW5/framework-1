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

## Django Template Language (ПР6)

Веб-интерфейс переведён с генерации HTML в Python на Django-шаблоны.

- Базовый шаблон: `templates/base.html` (блоки `{% block title %}`, `{% block content %}`)
- Навигация: `templates/includes/navigation.html`
- Карточка зала: `rooms/templates/rooms/includes/room_card.html`
- Статус брони: `bookings/templates/bookings/includes/booking_status.html`
- Именованные URL: `{% url 'rooms:detail' room.id %}`
- Фильтры: `{{ rooms|length }}`, `{{ room.name|default:"Без названия" }}`
- Статика: `homepage/static/homepage/css/style.css`, `js/main.js`, `img/logo.png`

Функция `page()` из ПР5 полностью удалена — HTML теперь в шаблонах.
