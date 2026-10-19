"""View-функции приложения homepage."""

from django.http import HttpResponse


def page(title: str, content: str) -> str:
    """Собрать HTML-документ с общим каркасом (Bootstrap, навигация)."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
    <nav class="nav nav-pills bg-light p-3 mb-4">
        <a class="nav-link" href="/">Главная</a>
        <a class="nav-link" href="/rooms/">Залы</a>
        <a class="nav-link" href="/bookings/">Бронирования</a>
    </nav>
    <main class="container">
        {content}
    </main>
</body>
</html>"""


def index(request):
    """Главная страница проекта."""
    content = """
    <h1 class="display-4">Сервис управления фотостудией</h1>
    <p class="lead">Приложение для управления залами фотостудии и бронированиями.</p>
    <p>Основные разделы:</p>
    <a href="/rooms/" class="btn btn-primary me-2">Залы</a>
    <a href="/bookings/" class="btn btn-secondary">Бронирования</a>
    """
    return HttpResponse(page("Фотостудия", content))


def page_not_found(request, exception):
    """Собственная страница 404."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
