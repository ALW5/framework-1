"""View-функции приложения rooms."""

from datetime import date

from django.http import HttpResponse

from homepage.views import page
from models.bookings import is_room_available
from models.rooms import find_room_by_id
from storage import load_bookings, load_clients, load_rooms


def rooms(request):
    """Список залов из data/rooms.json."""
    items = ""
    for room in load_rooms("data/rooms.json"):
        text = f"{room.name} — вместимость {room.capacity} мест"
        items += (
            f'<li class="list-group-item">'
            f'<a href="/rooms/{room.id}/">{text}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Залы фотостудии</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Фотостудия — залы", content))


def room_detail(request, room_id: int):
    """Карточка зала с проверкой доступности на сегодня."""
    rooms_list = load_rooms("data/rooms.json")
    room = find_room_by_id(rooms_list, room_id)

    if room is None:
        content = """
        <h1 class="text-danger">Зал не найден</h1>
        <a href="/rooms/" class="btn btn-outline-secondary">
            ← к списку залов
        </a>
        """
        return HttpResponse(
            page("Зал не найден", content),
            status=404,
        )

    clients_list = load_clients("data/clients.json")
    bookings_list = load_bookings(
        "data/bookings.json", rooms_list, clients_list
    )
    available = is_room_available(bookings_list, room, date.today().isoformat())
    status = "доступен" if available else "занят"
    badge = "bg-success" if available else "bg-danger"

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{room.name}</h5>
            <p class="card-text"><strong>ID:</strong> {room.id}</p>
            <p class="card-text"><strong>Студия:</strong> {room.studio}</p>
            <p class="card-text"><strong>Вместимость:</strong> {room.capacity} мест</p>
            <p class="card-text"><strong>Цена:</strong> {room.price_per_hour} руб/час</p>
            <p class="card-text">
                Доступность на текущую дату:
                <span class="badge {badge}">{status}</span>
            </p>
            <a href="/rooms/" class="btn btn-outline-secondary">
                ← к списку залов
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(room.name, content), status=200)
