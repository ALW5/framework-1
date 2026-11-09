"""View-функции приложения bookings."""

import sqlite3
from django.shortcuts import render

DB_PATH = "data/roomly.sqlite"


def bookings(request):
    """Список активных броней с JOIN."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    bookings_data = conn.execute("""
        SELECT 
            bookings.id, 
            bookings.booking_date, 
            rooms.name AS room_name, 
            rooms.capacity,
            clients.name AS client_name 
        FROM bookings
        JOIN rooms ON bookings.room_id = rooms.id
        JOIN clients ON bookings.client_id = clients.id
        WHERE bookings.is_cancelled = 0
        ORDER BY bookings.booking_date;
    """).fetchall()
    conn.close()
    
    return render(request, "bookings/booking_list.html", {"bookings": bookings_data})


def statistics(request):
    """Статистика по залам (GROUP BY)."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    stats = conn.execute("""
        SELECT 
            rooms.name AS room_name, 
            COUNT(bookings.id) AS bookings_count
        FROM rooms 
        LEFT JOIN bookings ON rooms.id = bookings.room_id AND bookings.is_cancelled = 0
        GROUP BY rooms.id, rooms.name
        ORDER BY bookings_count DESC;
    """).fetchall()
    conn.close()
    
    return render(request, "bookings/statistics.html", {"statistics": stats})
