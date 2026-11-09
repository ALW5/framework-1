"""Перенос данных из JSON в SQLite."""

import json

from db.database import get_connection

ROOMS_FILE = "data/rooms.json"
CLIENTS_FILE = "data/clients.json"
BOOKINGS_FILE = "data/bookings.json"


def load_json(filename: str) -> list:
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def import_rooms(conn):
    rooms = load_json(ROOMS_FILE)
    conn.executemany(
        """
        INSERT INTO rooms (id, name, studio, capacity, price_per_hour)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (r["id"], r["name"], r["studio"], r["capacity"], r["price_per_hour"])
            for r in rooms
        ],
    )


def import_clients(conn):
    clients = load_json(CLIENTS_FILE)
    conn.executemany(
        """
        INSERT INTO clients (id, name, email, phone)
        VALUES (?, ?, ?, ?)
        """,
        [(c["id"], c["name"], c["email"], c["phone"]) for c in clients],
    )


def import_bookings(conn):
    bookings = load_json(BOOKINGS_FILE)
    conn.executemany(
        """
        INSERT INTO bookings (id, room_id, client_id, booking_date, is_cancelled)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                b["id"],
                b["room_id"],
                b["client_id"],
                b["booking_date"],
                int(b["is_cancelled"]),
            )
            for b in bookings
        ],
    )


def main():
    conn = get_connection()
    try:
        import_rooms(conn)
        import_clients(conn)
        import_bookings(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()