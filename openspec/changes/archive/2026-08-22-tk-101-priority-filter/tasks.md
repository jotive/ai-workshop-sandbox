## 1. API

- [x] 1.1 En `api/routes/tickets.py`, agregar query param opcional `priority: TicketPriority | None = None` a `list_tickets` y pasarlo a `controller.list(priority)`.
- [x] 1.2 En `api/controllers/ticket_controller.py`, aceptar `priority` en `TicketController.list()` y pasarlo tal cual a `TicketService.list_tickets()` (ya acepta el parámetro).
- [x] 1.3 Confirmar que `TicketRepository.find_all()` ya filtra correctamente (no requiere cambios de datos).

## 2. Front

- [x] 2.1 En `front/index.html`, agregar un `<select>` de prioridad sobre la lista (`all`/`low`/`medium`/`high`) que dispare un nuevo `fetch` a `/tickets?priority=<valor>` al cambiar, omitiendo el query param cuando sea `all`.

## 3. Tests

- [x] 3.1 Agregar test de integración en `tests/integration/test_tickets_api.py`: crear tickets de distinta prioridad y verificar que `GET /tickets?priority=high` devuelve solo esos.
- [x] 3.2 Correr `pytest` completo en verde, incluyendo el nuevo test de filtro.

## Criterio de éxito (verificado)

- `pytest` en verde, incluyendo el nuevo test de filtro.
- `GET /tickets?priority=high` contra la API corriendo con `uvicorn` devuelve únicamente tickets `high` (verificado manualmente con `curl` además del test automatizado).
- El `<select>` del front filtra la lista visible sin recargar la página.
