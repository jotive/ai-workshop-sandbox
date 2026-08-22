# Plan — TK-103

> Se revisa ANTES de implementar. Corregir esto es barato; corregir código ya escrito es caro.

## Pasos

1. `api/db.py`: agregar columna `assignee TEXT` (nullable) al `SCHEMA` de `tickets`.
2. `api/schemas/ticket.py`: agregar `assignee: str | None = None` a `TicketCreateRequest` y a `TicketResponse`; agregar un DTO nuevo `TicketAssignRequest { assignee: str }` (requerido, no puede reasignarse a vacío).
3. `api/repositories/ticket_repository.py`: `create()` acepta `assignee` opcional y lo inserta; agregar `assign(ticket_id, assignee) -> Row` que hace `UPDATE tickets SET assignee = ? WHERE id = ?`.
4. `api/services/ticket_service.py`: `create_ticket()` pasa `request.assignee` al repositorio; agregar `assign_ticket(ticket_id, assignee)` que reusa el mismo chequeo de "no existe" que `close_ticket()` (levanta `TicketNotFoundError`).
5. `api/controllers/ticket_controller.py`: incluir `assignee` en `_to_ticket_response`; agregar método `assign()`.
6. `api/routes/tickets.py`: agregar `POST /tickets/{ticket_id}/assign` con body `TicketAssignRequest`.
7. `front/index.html`: agregar input de "Asignado a" (opcional) en el formulario de creación; mostrar el assignee (o "sin asignar") en cada card de ticket; agregar un botón "Reasignar" que pida el nuevo assignee y llame al endpoint nuevo.
8. Tests: unitarios en `tests/unit/test_ticket_repository.py` (crear con/sin assignee, `assign()` actualiza) y `tests/unit/test_ticket_service.py` (`assign_ticket` actualiza y levanta `TicketNotFoundError` si no existe); integración en `tests/integration/test_tickets_api.py` (crear con assignee, reasignar, reasignar ticket inexistente devuelve 404).

## Criterio de éxito

- `pytest` en verde, incluyendo todos los tests nuevos de `assignee`.
- `POST /tickets` con `assignee` en el body lo persiste y lo devuelve en la respuesta; sin `assignee` devuelve `null`.
- `POST /tickets/{id}/assign` actualiza el campo y lo refleja en `GET /tickets` inmediatamente después.
- El front permite crear un ticket con assignee y reasignarlo sin recargar la página.

## Qué NO entra en este ticket

- Entidad "usuario"/autenticación por persona — `assignee` sigue siendo texto libre, no una referencia a una tabla de usuarios.
- Notificar al assignee (email, webhook, etc.) — no se pidió.
- Filtrar el listado por assignee (como TK-101 hizo con prioridad) — es un ticket aparte si se necesita.
