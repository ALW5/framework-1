"""View-функции приложения bookings."""

from django.shortcuts import render

from models.bookings import find_booking_by_id
from storage import load_bookings, load_clients, load_rooms


def bookings(request):
    """Список броней."""
    rooms_list = load_rooms("data/rooms.json")
    clients_list = load_clients("data/clients.json")
    bookings_list = load_bookings(
        "data/bookings.json", rooms_list, clients_list
    )
    context = {"bookings": bookings_list}
    return render(request, "bookings/booking_list.html", context)


def booking_detail(request, booking_id: int):
    """Карточка брони."""
    rooms_list = load_rooms("data/rooms.json")
    clients_list = load_clients("data/clients.json")
    bookings_list = load_bookings(
        "data/bookings.json", rooms_list, clients_list
    )
    booking = find_booking_by_id(bookings_list, booking_id)
    context = {"booking": booking}
    return render(
        request,
        "bookings/booking_detail.html",
        context,
        status=404 if booking is None else 200,
    )
