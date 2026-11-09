"""View-функции приложения rooms."""

import sqlite3
from django.shortcuts import render

DB_PATH = "data/roomly.sqlite"


def rooms(request):
    """Список залов из SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rooms_list = conn.execute("""
        SELECT id, name, studio, capacity, price_per_hour 
        FROM rooms 
        ORDER BY name;
    """).fetchall()
    conn.close()
    
    return render(request, "rooms/room_list.html", {"rooms": rooms_list})


def available_rooms(request):
    """Поиск свободных залов на дату."""
    booking_date = request.GET.get("date")
    rooms = []
    
    if booking_date:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        rooms = conn.execute("""
            SELECT id, name, capacity 
            FROM rooms 
            WHERE id NOT IN (
                SELECT room_id FROM bookings 
                WHERE booking_date = ? AND is_cancelled = 0
            ) ORDER BY name;
        """, [booking_date]).fetchall()
        conn.close()
        
    return render(request, "rooms/available.html", {
        "rooms": rooms,
        "booking_date": booking_date
    })
