"""Тесты класса Client."""

from models import Client
from models.clients import add_client, find_client


def test_client_creation():
    client = Client(1, "Иван", "ivan@example.com", "+79990001122")
    assert client.id == 1
    assert client.name == "Иван"


def test_client_from_data():
    data = {
        "id": 1,
        "name": "Иван",
        "email": "ivan@example.com",
        "phone": "+79990001122",
    }
    client = Client.from_data(data)
    assert client.name == "Иван"


def test_add_client():
    clients = []
    add_client(clients, "Иван", "ivan@example.com", "+79990001122")
    assert len(clients) == 1


def test_find_client():
    clients = []
    add_client(clients, "Иван", "ivan@example.com", "+79990001122")
    assert len(find_client(clients, "иван")) == 1
    assert len(find_client(clients, "ivan@")) == 1
