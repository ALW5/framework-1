"""Маршруты приложения rooms."""

from django.urls import path

from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.rooms, name="list"),
    path("available/", views.available_rooms, name="available"), # ← новый
    # path("<int:room_id>/", ...)  # (можно оставить, если нужно)
]

