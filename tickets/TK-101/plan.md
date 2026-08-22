# Plan — TK-101

> Se revisa ANTES de implementar. Corregir esto es barato; corregir código ya escrito es caro.

## Pasos

1. En `api/routes/tickets.py`, agregar query param opcional `priority: TicketPriority | None = None` a `list_tickets` y pasarlo a `controller.list(priority)`.
2. En `api/controllers/ticket_controller.py`, aceptar `priority` en `TicketController.list()` y pasarlo tal cual a `TicketService.list_tickets()` (ya acepta el parámetro).
3. Confirmar que `TicketRepository.find_all()` ya filtra correctamente (no requiere cambios de datos).
4. En `front/index.html`, agregar un `<select>` de prioridad sobre la lista (`all`/`low`/`medium`/`high`) que dispare un nuevo `fetch` a `/tickets?priority=<valor>` al cambiar, omitiendo el query param cuando sea `all`.
5. Agregar test de integración en `tests/integration/test_tickets_api.py`: crear tickets de distinta prioridad y verificar que `GET /tickets?priority=high` devuelve solo esos.

## Criterio de éxito

- `pytest` en verde, incluyendo el nuevo test de filtro.
- `GET /tickets?priority=high` contra la API corriendo con `uvicorn` devuelve únicamente tickets `high` (verificado manualmente con `curl` además del test automatizado).
- El `<select>` del front filtra la lista visible sin recargar la página.

## Qué NO entra en este ticket

- Filtrar por múltiples prioridades a la vez (ej. `high,medium`) — no se pidió.
- Filtrar por estado — eso ya funciona indirectamente cerrando tickets, no es parte de este ticket.
- Ordenar el listado por prioridad — el orden sigue siendo por `id DESC`.
