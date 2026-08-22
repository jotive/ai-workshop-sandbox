## 1. Fix

- [x] 1.1 En `api/repositories/ticket_repository.py::count_open()`, filtrar por `WHERE status = ?` con `TicketStatus.OPEN.value`, siguiendo el mismo patrón que `count_closed()`.

## 2. Tests

- [x] 2.1 Agregar test unitario en `tests/unit/test_ticket_repository.py` que cree un ticket abierto y uno cerrado, y verifique que `count_open()` devuelve 1 (no 2).
- [x] 2.2 Agregar test de integración en `tests/integration/test_tickets_api.py` que cree dos tickets, cierre uno, y verifique que `GET /stats` devuelve `open: 1`, `closed: 1`, `total: 2`.
- [x] 2.3 Correr `pytest` completo y confirmar que no se rompió nada más (en particular `count_total()`, que sigue contando todos los tickets sin filtrar).

## Criterio de éxito (verificado)

- `pytest` en verde, incluyendo los dos tests nuevos.
- `GET /stats` contra la API corriendo con `uvicorn`, después de cerrar al menos un ticket, muestra `open` estrictamente menor que `total`.
