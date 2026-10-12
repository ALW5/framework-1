"""Модель клиента фотостудии и функции работы с клиентами."""

from typing import List, Optional


class Client:
    """Клиент фотостудии."""

    def __init__(
        self,
        client_id: int,
        name: str,
        email: str,
        phone: str,
    ) -> None:
        """Создать объект клиента."""
        self.id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        """Вернуть строковое представление клиента."""
        return f"{self.name} ({self.email}, {self.phone})"

    @classmethod
    def from_data(cls, data: dict) -> "Client":
        """Создать клиента из данных JSON."""
        return cls(
            client_id=data["id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
        )


def add_client(
    clients: List[Client],
    name: str,
    email: str,
    phone: str,
) -> Client:
    """Создать клиента и добавить в коллекцию."""
    new_id = max((c.id for c in clients), default=0) + 1
    client = Client(new_id, name, email, phone)
    clients.append(client)
    return client


def find_client(clients: List[Client], query: str) -> List[Client]:
    """Найти клиентов по имени или email."""
    query_lower = query.lower()
    return [
        c for c in clients
        if query_lower in c.name.lower()
        or query_lower in c.email.lower()
    ]


def find_client_by_id(
    clients: List[Client], client_id: int
) -> Optional[Client]:
    """Найти клиента по id."""
    for client in clients:
        if client.id == client_id:
            return client
    return None
