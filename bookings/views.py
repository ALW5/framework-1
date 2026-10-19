"""View-функции приложения bookings."""

from django.http import HttpResponse

from homepage.views import page
from models.bookings import find_booking_by_id
from storage import load_bookings, load_clients, load_rooms


def bookings(request):
    """Список броней из data/bookings.json."""
    rooms_list = load_rooms("data/rooms.json")
    clients_list = load_clients("data/clients.json")
    bookings_list = load_bookings(
        "data/bookings.json", rooms_list, clients_list
    )

    items = ""
    for booking in bookings_list:
        status = "отменено" if booking.is_cancelled else "активно"
        badge = "bg-secondary" if booking.is_cancelled else "bg-success"
        items += f"""
        <li class="list-group-item">
            <a href="/bookings/{booking.id}/">
                {booking.room.name} — {booking.booking_date}
            </a>
            <span class="badge {badge}">{status}</span>
        </li>
        """

    content = f"""
    <h1>Бронирования</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Фотостудия — бронирования", content))


def booking_detail(request, booking_id: int):
    """Карточка брони с связанными залом и клиентом."""
    rooms_list = load_rooms("data/rooms.json")
    clients_list = load_clients("data/clients.json")
    bookings_list = load_bookings(
        "data/bookings.json", rooms_list, clients_list
    )
    booking = find_booking_by_id(bookings_list, booking_id)

    if booking is None:
        content = """
        <h1 class="text-danger">Бронирование не найдено</h1>
        <a href="/bookings/" class="btn btn-outline-secondary">
            ← к списку броней
        </a>
        """
        return HttpResponse(
            page("Бронирование не найдено", content),
            status=404,
        )

    status = "отменено" if booking.is_cancelled else "активно"
    badge = "bg-secondary" if booking.is_cancelled else "bg-success"

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Бронирование №{booking.id}</h5>
            <p class="card-text"><strong>Зал:</strong> {booking.room.name}</p>
            <p class="card-text"><strong>Дата:</strong> {booking.booking_date}</p>
            <p class="card-text"><strong>Клиент:</strong> {booking.client.name}</p>
            <p class="card-text">
                Статус: <span class="badge {badge}">{status}</span>
            </p>
            <a href="/bookings/" class="btn btn-outline-secondary">
                ← к списку броней
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Бронирование №{booking.id}", content), status=200)
