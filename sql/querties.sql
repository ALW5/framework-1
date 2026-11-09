-- 1. Список всех залов (Выборка)
SELECT id, name, studio, capacity, price_per_hour FROM rooms ORDER BY name;

-- 2. Список всех клиентов (Выборка)
SELECT id, name, email, phone FROM clients ORDER BY name;

-- 3. Поиск залов по вместимости (Фильтрация WHERE)
SELECT id, name, capacity FROM rooms WHERE capacity >= 10 ORDER BY capacity;

-- 4. Поиск активных бронирований (Фильтрация WHERE)
SELECT id, room_id, client_id, booking_date FROM bookings WHERE is_cancelled = 0;

-- 5. Бронирования с названиями залов и именами клиентов (JOIN)
SELECT 
    bookings.id, 
    bookings.booking_date, 
    rooms.name AS room_name, 
    clients.name AS client_name 
FROM bookings
JOIN rooms ON bookings.room_id = rooms.id
JOIN clients ON bookings.client_id = clients.id
WHERE bookings.is_cancelled = 0
ORDER BY bookings.booking_date;

-- 6. Свободные залы на выбранную дату (JOIN + Подзапрос)
SELECT id, name, capacity 
FROM rooms 
WHERE id NOT IN (
    SELECT room_id FROM bookings 
    WHERE booking_date = '2026-09-20' AND is_cancelled = 0
) ORDER BY name;

-- 7. Общее количество залов (Агрегатная функция)
SELECT COUNT(*) AS rooms_count FROM rooms;

-- 8. Общее количество активных броней (Агрегатная функция)
SELECT COUNT(*) AS active_bookings FROM bookings WHERE is_cancelled = 0;

-- 9. Количество броней по каждому залу (Группировка GROUP BY)
SELECT 
    rooms.name AS room_name, 
    COUNT(bookings.id) AS bookings_count
FROM rooms 
LEFT JOIN bookings ON rooms.id = bookings.room_id AND bookings.is_cancelled = 0
GROUP BY rooms.id, rooms.name
ORDER BY bookings_count DESC;

-- 10. Клиенты, сделавшие более 1 брони (Группировка + HAVING)
SELECT 
    clients.name AS client_name, 
    COUNT(bookings.id) AS total_bookings
FROM clients
JOIN bookings ON clients.id = bookings.client_id
WHERE bookings.is_cancelled = 0
GROUP BY clients.id, clients.name
HAVING COUNT(bookings.id) > 1
ORDER BY total_bookings DESC;